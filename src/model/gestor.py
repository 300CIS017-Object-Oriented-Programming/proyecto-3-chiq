from abc import ABC, abstractmethod

class Gestor(ABC):

        @abstractmethod
        def __init__(self):
            pass

        @abstractmethod
        def create_file(self, path, content):
            pass

        @abstractmethod
        def read_file(self, path):
            pass

        @abstractmethod
        def update_file(self, path, content):
            pass


