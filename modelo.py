import sqlite3
from entidades import ValidacionError, Venta 
from decoradores import log_operacion, log_errores_bd 
from exepciones import BDError

class VentasModelo:
    def __init__(self, db_name="venta_semillas.db"):
        self.db_name = db_name
        self.crear_tabla()
    
    @log_operacion 
    def conectar_bd(self):
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            raise BDError(f"Error conectando a la base de datos: {e}")
    
    @log_operacion 
    @log_errores_bd 
    def crear_tabla(self):
        try:
            conex = self.conectar_bd()
            cursor = conex.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS ventas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cultivar TEXT,
                    cantidad INTEGER,
                    cliente TEXT,
                    telefono TEXT,
                    vendedor TEXT,
                    fecha TEXT
                )"""
            )
            conex.commit()
            conex.close()
        except sqlite3.Error as e:
            raise BDError(f"Error creando la tabla: {e}")
    
    @log_operacion
    @log_errores_bd
    def get_ventas(self):
        try:
            conex = self.conectar_bd()
            cursor = conex.cursor()
            cursor.execute("SELECT * FROM ventas")
            ventas_data = cursor.fetchall()
            conex.close()
            
            return [Venta.from_tuple(venta_data) for venta_data in ventas_data]
        except sqlite3.Error as e:
            raise BDError(f"Error obteniendo ventas: {e}")
    
    @log_operacion
    @log_errores_bd
    def agregar_venta(self, venta: Venta): 
        venta.validar() 
        try:
            conex = self.conectar_bd()
            cursor = conex.cursor()
            cursor.execute(
                """INSERT INTO ventas (cultivar, cantidad, cliente, telefono, vendedor, fecha)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                venta.to_tuple() 
            )
            conex.commit()
            conex.close()
        except sqlite3.Error as e:
            raise BDError(f"Error al agregar la venta: {e}")
    
    @log_operacion
    @log_errores_bd
    def eliminar_venta(self, venta_id):
        try:
            conex = self.conectar_bd()
            cursor = conex.cursor()
            cursor.execute("DELETE FROM ventas WHERE id = ?", (venta_id,))
            if cursor.rowcount == 0:
                raise BDError("No se encontró la venta a eliminar.")
            conex.commit()
            conex.close()
        except sqlite3.Error as e:
            raise BDError(f"Error al eliminar la venta: {e}")
    
    @log_operacion
    @log_errores_bd
    def modificar_venta(self, venta: Venta): 
        venta.validar() 
        if venta.id is None:
            raise ValidacionError("Se requiere un ID para modificar la venta.")
        try:
            conex = self.conectar_bd()
            cursor = conex.cursor()
            cursor.execute(
                """UPDATE ventas 
                   SET cultivar = ?, cantidad = ?, cliente = ?, telefono = ?, vendedor = ?, fecha = ?
                   WHERE id = ?""",
                venta.to_tuple(include_id=True) 
            )
            if cursor.rowcount == 0:
                raise BDError("No se encontró la venta para modificar.")
            conex.commit()
            conex.close()
        except sqlite3.Error as e:
            raise BDError(f"Error al modificar la venta: {e}")
    
    @log_operacion
    @log_errores_bd
    def obtener_venta(self, venta_id):
        try:
            conex = self.conectar_bd()
            cursor = conex.cursor()
            cursor.execute("SELECT * FROM ventas WHERE id = ?", (venta_id,))
            venta_data = cursor.fetchone()
            conex.close()
            if not venta_data:
                raise BDError("Venta no encontrada.")
            return Venta.from_tuple(venta_data) 
        except sqlite3.Error as e:
            raise BDError(f"Error obteniendo la venta: {e}")