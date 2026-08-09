from entidades import Venta, ValidacionError 
from modelo import VentasModelo
from exepciones import BDError
from vista import VentasVista
from decoradores import log_operacion 

class VentasControlador:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_agregar_callback(self.agregar_venta)
        self.view.set_ver_callback(self.ver_ventas)
        self.view.set_eliminar_callback(self.eliminar_venta)
        self.view.set_modificar_callback(self.modificar_venta)

        self.ver_ventas()

# loggin para cuando se agrega una venta

    @log_operacion 
    def agregar_venta(self):
        data = self.view.get_input_data()
        try:
            nueva_venta = Venta(
                cultivar=data['cultivar'],
                cantidad=data['cantidad'], 
                cliente=data['cliente'],
                telefono=data['telefono'],
                vendedor=data['vendedor'],
                fecha=data['fecha']
            )
            self.model.agregar_venta(nueva_venta) 
            self.view.mostrar_message_info("¡Felicidades!", "Nueva venta registrada!")
            self.view.limpiar_campos()
            self.ver_ventas()
        except (ValidacionError, BDError) as e:
            self.view.mostrar_message_warning("¡ERROR!", str(e))
        except Exception as e: 
            self.view.mostrar_message_warning("¡ERROR INESPERADO!", f"Ocurrió un error: {e}")
    
# loggin para cuando solicite ver ventas

    @log_operacion 
    def ver_ventas(self):
        try:
            ventas = self.model.get_ventas() 
            self.view.actualizar_treeview(ventas)
        except BDError as e:
            self.view.mostrar_message_warning("Error de Base de Datos", str(e))
        except Exception as e:
            self.view.mostrar_message_warning("Error Inesperado", f"Ocurrió un error: {e}")

# loggin para eliminar venta
#            
    @log_operacion 
    def eliminar_venta(self):
        venta_id = self.view.get_selected_venta_id()
        if not venta_id:
            self.view.mostrar_message_warning("¡ERROR!", "Seleccione una venta para eliminar.")
            return
        try:
            self.model.eliminar_venta(venta_id)
            self.view.mostrar_message_info("Éxito", "Venta eliminada.")
            self.ver_ventas() 
        except BDError as e:
            self.view.mostrar_message_warning("Error de Base de Datos", str(e))
        except Exception as e:
            self.view.mostrar_message_warning("Error Inesperado", f"Ocurrió un error: {e}")
    
    # loggin para modificar venta
    @log_operacion 
    def modificar_venta(self):
        venta_id = self.view.get_selected_venta_id()
        if not venta_id:
            self.view.mostrar_message_warning("¡ERROR!", "Seleccione una venta para modificar.")
            return
        
        try:
            venta_existente = self.model.obtener_venta(venta_id)
        except BDError as e:
            self.view.mostrar_message_warning("Error de Base de Datos", str(e))
            return
        except Exception as e:
            self.view.mostrar_message_warning("Error Inesperado", f"Ocurrió un error: {e}")
            return
            
        data = self.view.get_input_data()

        # Actualizar los atributos del objeto Venta con los datos de entrada
        # solamente si el campo de entrada no está vacío

        if data['cultivar']: venta_existente.cultivar = data['cultivar']
        if data['cantidad']: venta_existente.cantidad = data['cantidad']
        if data['cliente']: venta_existente.cliente = data['cliente']
        if data['telefono']: venta_existente.telefono = data['telefono']
        if data['vendedor']: venta_existente.vendedor = data['vendedor']
        if data['fecha']: venta_existente.fecha = data['fecha']

        try:
            self.model.modificar_venta(venta_existente)
            self.view.mostrar_message_info("Éxito", "Venta modificada exitosamente.")
            self.view.limpiar_campos()
            self.ver_ventas()
        except (ValidacionError, BDError) as e:
            self.view.mostrar_message_warning("Error", str(e))
        except Exception as e:
            self.view.mostrar_message_warning("Error Inesperado", f"Ocurrió un error: {e}")