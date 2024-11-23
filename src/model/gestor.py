from abc import ABC, abstractmethod


class Gestor(ABC):

        @abstractmethod
        def __init__(self):
            pass

        def detectar_delimitador(self, data:str):
            pass

        @abstractmethod
        def leer_programas(self, path):
            pass

        @abstractmethod
        def create_file(self, path, content):
            pass

        @abstractmethod
        def read_file(self, path_base, anio, col_cod_snies):
            pass

        @abstractmethod
        def update_file(self, path, content):
            pass


