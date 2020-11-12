#! /usr/bin/env python3
from cliente import Cliente

class ClienteParticular(Cliente):
    '''Representa un cliente particular'''
    def __init__(self, nombre, apellido, telefono, mail, id_cliente = None):
        self.nombre = nombre
        self.apellido = apellido
        super().__init__(telefono, mail, id_cliente)

    def __str__(self):
        cadena = f"Cliente nro: {self.id_cliente}\n"
        cadena += f"Tipo de cliente: Particular\n"
        cadena += f"Nombre: {self.nombre} {self.apellido}\n"
        cadena += f"Teléfono: {self.telefono} - e-mail: {self.mail}\n"
        return cadena     
