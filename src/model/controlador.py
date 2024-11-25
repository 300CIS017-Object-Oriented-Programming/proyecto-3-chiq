from model.gestor import Gestor
from model.gestor_json import GestorJSON
from model.gestor_csv import GestorCSV
from model.gestor_xlsx import GestorXLSX
from model.programa_academico import ProgramaAcademico
from settings import ruta1, ruta4, ruta7, ruta10, ruta13, ruta16


'''
Consideraciones con adherencia de streamlit al proyecto respecto a los archivos subidos en memoria 

Se puede tomar dos caminos, tomar los datos de manera temporal con la memoria de streamlit
mientras que la página es ejecutada

sol con memoria temporal: Para cada archivo subido, lee el archivo en un DataFrame y almacena el DataFrame en el diccionario usando el nombre del archivo como clave.

archivos_procesados[uploaded_file.name] = df: Almacena el DataFrame en el diccionario.Para cada archivo subido, lee el archivo en un DataFrame y almacena el DataFrame en el diccionario usando el nombre del archivo como clave.

archivos_procesados[uploaded_file.name] = df: Almacena el DataFrame en el diccionario.

Ó

Se pueden descargar los archivos y utilizaros de manera local en el codigo fuente


Esto esta sujeto a elección como sea más conveniente

'''

class SNIESController:
    def __init__(self):
        gestor_csv = GestorCSV()
        gestor_xlsx = GestorXLSX()
        gestor_json = GestorJSON()
        self.gestores: list[Gestor] = [gestor_csv, gestor_xlsx, gestor_json]
        self.programas_academicos: dict[int, ProgramaAcademico()]  # Inicializar el diccionario de programas académicos
    '''
    def procesar_tipo_output(self, opcion, ruta_output, programas_academicos, etiquetas_columnas, ano_inicio, ano_fin):
        archivo_creado = False
        try:
            if opcion == 1:  # CSV
                print("Exportando archivo resultado.csv...")
                archivo_creado = self.gestor_csv_obj.crear_archivo_csv(ruta_output, programas_academicos, etiquetas_columnas, ano_inicio, ano_fin)
            elif opcion == 2:  # TXT
                print("Exportando archivo resultado.txt...")
                archivo_creado = self.gestor_txt_obj.crear_archivo_txt(ruta_output, programas_academicos, etiquetas_columnas, ano_inicio, ano_fin)
            elif opcion == 3:  # JSON
                print("Exportando archivo resultado.json...")
                archivo_creado = self.gestor_json_obj.crear_archivo_json(ruta_output, programas_academicos, etiquetas_columnas, ano_inicio, ano_fin)
            elif opcion == 4:  # Ninguna
                print("No se ha creado ningún archivo.")
            else:
                raise ValueError("Opción inválida. Debe ingresar un valor entre 1 y 4.")
        except Exception as e:
            print(f"Error: {e}")
        else:
            return archivo_creado
        '''

    @staticmethod
    def procesar_datos_csv(self, anio_actual, anio_siguiente, opcion_output, ano_inicio, ano_fin):
        ruta_programas = ruta16 + ".xlsx"
        ruta_admitidos = ruta1 + str(anio_actual) + ".xlsx"
        ruta_graduados = ruta4 + str(anio_actual) + ".xlsx"
        ruta_inscritos = ruta7 + str(anio_actual) + ".xlsx"
        ruta_matriculados = ruta10 + str(anio_actual) + ".xlsx"
        ruta_matriculados_primer_semestre = ruta13 + str(anio_actual) + ".xlsx"
        codigos_snies = self.gestor_xlsx.leer_programas(ruta_programas)


