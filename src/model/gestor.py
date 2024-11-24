from abc import ABC, abstractmethod

# Para darle un formato al diccionario de programas academicos

from typing import Dict

from programa_academico import ProgramaAcademico


class Gestor(ABC):

        @abstractmethod
        def __init__(self):
            pass

        def detectar_delimitador(self, data:str):
            pass

        @abstractmethod
        def leer_programas(self, path):
            pass


        # Tener en cuenta que para el siguiente metodo content es el data frame que vamos a usar para obtener las etiquetas
        @abstractmethod
        def create_file(self, path, content, programas_academicos : Dict[int, ProgramaAcademico()], ano1, ano2):
            pass

        @abstractmethod
        def read_file(self, path_base, anio, col_cod_snies):
            pass

        @abstractmethod
        def update_file(self, path, content):
            pass


