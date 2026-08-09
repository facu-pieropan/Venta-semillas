import re

class ValidacionError(Exception):
    pass

class Venta:
    def __init__(self, id=None, cultivar=None, cantidad=None, cliente=None, telefono=None, vendedor=None, fecha=None):
        self.id = id 
        self.cultivar = cultivar
        self.cantidad = cantidad
        self.cliente = cliente
        self.telefono = telefono
        self.vendedor = vendedor
        self.fecha = fecha

    def validar(self):
        if not self.cultivar:
            raise ValidacionError("El campo 'Cultivar' no puede estar vacío.")
        if not self.cantidad:
            raise ValidacionError("El campo 'Cantidad' no puede estar vacío.")
        try:
            self.cantidad = int(self.cantidad) 
            if self.cantidad <= 0:
                raise ValidacionError("La cantidad debe ser un número entero positivo.")
        except ValueError:
            raise ValidacionError("La cantidad debe ser un número entero.")

        if not self.cliente:
            raise ValidacionError("El campo 'Cliente' no puede estar vacío.")
        if not self.telefono:
            raise ValidacionError("El campo 'Teléfono' no puede estar vacío.")
        
        if not re.fullmatch(r'\d{10}', str(self.telefono)):
            raise ValidacionError("El número de teléfono debe contener 10 dígitos numéricos.")
        
        if not self.vendedor:
            raise ValidacionError("El campo 'Vendedor' no puede estar vacío.")
        if not self.fecha:
            raise ValidacionError("El campo 'Fecha' no puede estar vacío.")
       

    def to_tuple(self, include_id=False):
 
        data = (self.cultivar, self.cantidad, self.cliente, self.telefono, self.vendedor, self.fecha)
        if include_id:
            return data + (self.id,)
        return data

    @staticmethod
    def from_tuple(data_tuple):
    
        if len(data_tuple) == 7:
            return Venta(id=data_tuple[0], cultivar=data_tuple[1], cantidad=data_tuple[2],
                         cliente=data_tuple[3], telefono=data_tuple[4], vendedor=data_tuple[5],
                         fecha=data_tuple[6])
        return None 