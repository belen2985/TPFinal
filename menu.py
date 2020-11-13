#! /usr/bin/env python3
import sys
from listaClientes import ListaClientes

class Menu:
    '''Mostrar un menú y responder a las opciones'''
    def __init__(self):
        self.lista_clientes = ListaClientes()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.eliminar_cliente,
            "0": self.salir
        }

    def mostrar_menu(self):
        print("""
Menú del sistema:
1. Mostrar todos los clientes
2. Alta de cliente
3. Baja de cliente
0. Salir
""")

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))

    def mostrar_clientes(self, lista=None):
        if lista == None:
            lista = self.lista_clientes.lista
        for cliente in lista:
            print(cliente)
            print("=====================================")
            
    def nuevo_cliente(self):
        tipo = "A"
        while tipo not in ("C","c","P","p"):
            tipo = input ("Ingrese el tipo de cliente: C:Corporativo / P:Particular: ")
        nombre = input ("Ingrese el nombre: ")
        if tipo in ("C","c"):
            contacto = input("Ingrese el nombre del contacto: ")
            tc = input("Ingrese el teléfono del contacto: ")
        else:
            apellido = input("Ingrese el apellido: ") 
        tel = input("Ingrese el teléfono: ")
        mail = input("Ingrese el e-mail: ")
        if tipo in ("C","c"):
            c = self.lista_clientes.nuevo_cliente_corporativo(nombre, contacto, tc, tel, mail)
        else:
            c = self.lista_clientes.nuevo_cliente_particular(nombre, apellido, tel, mail)
        if c is None:
            print("Error al cargar el cliente")
        else:
            print("Cliente cargado con éxito")
            
    def eliminar_cliente(self):
        nc = input ("Ingrese el Nro de Cliente a dar de baja: ")
        eliminado = self.lista_clientes.eliminar_cliente(nc)
        if eliminado:
            print ("Cliente eliminado correctamente")
        else:
            print ("El cliente no se pudo eliminar")
    
    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

#Esta parte del código está fuera de la clase Menu.
#Si este archivo es el programa principal (es decir, si no ha sido importado
#desde otro módulo, sino ejecutado directamente), entonces llamamos al método
# ejecutar().
if __name__ == "__main__":
    Menu().ejecutar()
