#! /usr/bin/env python3
from listaTrabajos import ListaTrabajos
from cliente import Cliente
from clienteCorporativo import ClienteCorporativo
from clienteParticular import ClienteParticular
from trabajo import Trabajo
from repositorio import Repositorio
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos
import sys
from listaClientes import ListaClientes

class Menu:
    '''Mostrar un menú y responder a las opciones'''
    def __init__(self):
        self.lista_clientes = ListaClientes()
        self.lista_trabajos = ListaTrabajos()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.eliminar_cliente,
            "4": self.modificar_cliente,
            "5": self.mostrar_trabajos,
            "0": self.salir
        }

    def mostrar_menu(self):
        print("""
Menú del sistema:
1. Mostrar todos los clientes
2. Alta de cliente
3. Baja de cliente
4. Modificación de cliente
5. Mostrar todos los trabajos
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

    def modificar_cliente(self):
        nc = input ("Ingrese el Nro de Cliente a modificar: ")
        c = self.lista_clientes.rc.get_one(nc)
        
        if type(c) is ClienteCorporativo:
            c.nombre_empresa = input("Ingrese el nombre de la empresa: ")
            c.telefono = input("Ingrese el teléfono de la empresa: ")
            c.nombre_contacto = input("Ingrese el nombre del contacto: ")
            c.telefono_contacto = input("Ingrese el teléfono del contacto: ")
            c.mail = input("Ingrese el e-mail: ")
        else:
            c.nombre = input("Ingrese el nombre: ")
            c.apellido = input("Ingrese el apellido: ")
            c.telefono = input("Ingrese el teléfono: ")
            c.mail = input("Ingrese el e-mail: ")        
        modificado = self.lista_clientes.modificar_cliente(c)
        if modificado:
            print ("Cliente modificado correctamente")
        else:
            print ("El cliente no se pudo modificar")

    def mostrar_trabajos(self, lista=None):
        if lista == None:
            lista = self.lista_trabajos.lista
        for trabajo in lista:
            print(trabajo)
            print("=====================================")
    
    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

#Esta parte del código está fuera de la clase Menu.
#Si este archivo es el programa principal (es decir, si no ha sido importado
#desde otro módulo, sino ejecutado directamente), entonces llamamos al método
# ejecutar().
if __name__ == "__main__":
    Menu().ejecutar()
