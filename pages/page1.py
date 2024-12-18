import streamlit as st
#from src.model.gestor_csv import GestorCSV

# Aca se usa una ruta de importacion absoluta
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def app():
    st.markdown("<h1 style='text-align: center;'>SNIES DATA BASE</h1>", unsafe_allow_html=True)
    st.header("Bienvenido al SNIES data manager & análisis")

    # Para temas de pruebas esta la parte de abajo: es para ensayar el GestorCsv
    '''
    # Instancia de la clase GestorCsv
    gestor = GestorCSV()

    # Configura el título de la página
    st.subheader("Subir y procesar archivo CSV")

    # Usa el widget file_uploader para permitir la subida de archivos
    uploaded_file = st.file_uploader("Sube los archivos del SNIES para poder procesar los datos necesarios", type="csv")

    # Chequea si un archivo ha sido subido
    if uploaded_file is not None:
        # Cargar y procesar el archivo CSV usando la clase GestorCsv
        df = gestor.leer_programas(uploaded_file)

        # Muestra una vista previa del DataFrame
        st.write("Vista previa del archivo subido:")
        st.write(df)
    '''
