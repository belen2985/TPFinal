#! /usr/bin/python3

import datetime
from cliente import Cliente
from clienteCorporativo import ClienteCorporativo
from clienteParticular import ClienteParticular
from repositorio import Repositorio
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo

class ListaTrabajos:
    def __init__(self):
        self.rt = RepositorioTrabajos()
        self.lista = self.rt.get_all()

    def nuevo_trabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, fecha_entrega_real, descripcion, retirado):
        t = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, fecha_entrega_real, descripcion, retirado)
        t.id_trabajo = self.rt.store(t)
        if t.id_trabajo == 0:
            return None
        else:
            self.lista.append(t)
            return t