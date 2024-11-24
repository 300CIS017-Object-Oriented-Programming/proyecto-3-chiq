from model.gestor import Gestor
from model.gestorJSON import GestorJSON
from model.gestor_csv import GestorCSV
from model.gestorXLSX import GestorXLSX

class SNIESController:
    def __init__(self):
        gestor_csv = GestorCSV()
        gestor_xlsx = GestorXLSX()
        gestor_json = GestorJSON()
        self.gestores: list[Gestor] = [gestor_csv, gestor_xlsx, gestor_json]
        self.programas_academicos = {}  # Inicializar el diccionario de programas académicos

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

        return archivo_creado

