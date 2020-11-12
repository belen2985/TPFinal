#! /usr/bin/env python3
from cliente import Cliente

class ClienteCorporativo(Cliente):
    '''Representa un cliente particular'''
    def __init__(self, nombre_empresa, nombre_contacto, telefono_contacto,
            telefono, mail, id_cliente = None):
        self.nombre_empresa = nombre_empresa
        self.nombre_contacto = nombre_contacto
        self.telefono_contacto = telefono_contacto
        super().__init__(telefono, mail, id_cliente)

    def __str__(self):
        cadena = f"Cliente nro: {self.id_cliente}\n"
        cadena += f"Tipo de cliente: Corporativo\n"
        cadena += f"Nombre: {self.nombre_empresa}\n"
        cadena += f"Teléfono empresa: {self.telefono} - e-mail: {self.mail}\n"
        cadena += f"Contacto: {self.nombre_contacto} - Teléfono: {self.telefono_contacto}\n"
        return cadena
         
