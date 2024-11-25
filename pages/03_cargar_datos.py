import pandas as pd

# Aca se usa una ruta de importacion absoluta
import sys
import os

from model.settings import ruta1, ruta13

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import streamlit as st

'''
ruta1
ruta2
ruta3 
'''

def cargar_datos():
    st.title('Cargar datos')

    # Usa el widget file_uploader para permitir la subida de archivos
    uploaded_file = st.file_uploader("Sube los archivos del SNIES para poder procesar los datos necesarios", type="xlsx")

    # Chequea si un archivo ha sido subido
    if uploaded_file is not None:
        # Cargar y procesar el archivo CSV usando la clase GestorCsv
        df = pd.read_excel(uploaded_file)
        # Muestra una vista previa del DataFrame
        st.write("Vista previa del archivo subido:")
        st.write(df)

if __name__ == '__main__':
    cargar_datos()