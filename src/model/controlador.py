
from model.programa_academico import ProgramaAcademico
from model.consolidado import Consolidado
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

class Controlador:
    def __init__(self):
        self.programas_academicos = []
        self.datos = pd.DataFrame()
        self.resultados = pd.DataFrame()

    def cargar_programa_academico(self, data_frame):
        pass
        
    def procesar_datos(self, anios_seleccionados, programas_seleccionados):
        self.datos = cargar_datos(anios_seleccionados, programas_seleccionados)
        self.resultados = calcular_metricas(self.datos)

    def generar_visualizaciones(self, tipo_grafico, filtro):
        return generar_graficos(self.resultados, tipo_grafico, filtro)

    def exportar_resultados(self, formato, ruta_salida):
        exportar_datos(self.resultados, formato, ruta_salida)



