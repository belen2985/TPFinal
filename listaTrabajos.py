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