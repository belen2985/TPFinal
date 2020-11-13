#! /usr/bien/env python3
from cliente import Cliente
from clienteCorporativo import ClienteCorporativo
from clienteParticular import ClienteParticular
from repositorioClientes import RepositorioClientes

class ListaClientes:
    def __init__(self):
        self.rc = RepositorioClientes()
        self.lista = self.rc.get_all()

    def nuevo_cliente_corporativo(self, nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail):
        c = ClienteCorporativo(nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail)
        c.id_cliente = self.rc.store(c)
        if c.id_cliente == 0:
            return None
        else:
            self.lista.append(c)
            return c

    def nuevo_cliente_particular(self, nombre, apellido, telefono, mail):
        c = ClienteParticular(nombre, apellido, telefono, mail)
        c.id_cliente = self.rc.store(c)
        if c.id_cliente == 0:
            return None
        else:
            self.lista.append(c)
            return c

    def buscar_cliente(self, id_cliente):
        '''Recibe un id del cliente y lo busca en la lista, devuelve el cliente'''
        for c in self.lista:
            if c.id_cliente == id_cliente:
                break
        return c

    def eliminar_cliente(self, id_cliente):
        c = self.buscar_cliente(id_cliente)
        eliminado = self.rc.delete(c)
        if eliminado:
            self.lista.remove(c)
            return True
        else:
            return False

    def modificar_cliente(self, cliente):
        modificado = self.rc.update(cliente)
        if modificado:
            self.lista = self.rc.get_all()
            return True
        else:
            return False
