from model.gestor import Gestor
import pandas as pd
import re

class GestorCSV(Gestor):
    def __init__(self):
        pass

    def create_file(self, path, content):
        pass

    def leer_programas(self, path_base):
        try:
            data_read = pd.read_csv(path_base, sep=';')
            print("Archivo leído correctamente.")

        # Aqui se muestra la estructura de las excepciones que hay en la lectura de archivos

        except FileNotFoundError:
            print("Error: El archivo no se encuentra en la ruta especificada.")
        except pd.errors.EmptyDataError:
            print("Error: El archivo está vacío.")
        except pd.errors.ParserError:
            print("Error: Hay un problema al parsear el archivo.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
        else:
            # Itera sobre cada fila del DataFrame

            # nota: la columna 12 es la columna en donde esta el codigo snies del programa,
            # aunque con pandas podemos usar la etiqueta de la columna para poder filtrar
            # los datos que estan dentro de esta columna
            # fin nota.
            codigos_snies_return = []
            for index, row in data_read.iterrows():
                # print(row)  # Imprime la fila completa /// <---- esta linea se puede usar para terminos de pruebas
                codigo_snies = int(row['CÓDIGO SNIES DEL PROGRAMA'])  # Ajusta 'nombre_columna' al nombre de tu columna específica
                codigos_snies_return.append(codigo_snies)
            return codigos_snies_return


    def read_file(self, path_base, anio, col_cod_snies):
        path = path_base + anio + ".csv"
        data_read = pd.read_csv(path, sep=';')
        return data_read

    def update_file(self, path, content):
        pass

