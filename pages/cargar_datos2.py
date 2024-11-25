import pandas as pd
import sys
import os
import streamlit as st
from typing import Dict


def app():
    st.title('Cargar datos')

    # Actualiza las rutas según sea necesario
    ruta1 = "C:/proyecto-3-chiq/docs/inputs/admitidos"
    ruta2 = "C:/proyecto-3-chiq/docs/inputs/inscritos"
    ruta3 = "C:/proyecto-3-chiq/docs/inputs/graduados"
    ruta4 = "C:/proyecto-3-chiq/docs/inputs/matriculados"
    ruta5 = "C:/proyecto-3-chiq/docs/inputs/matriculadosPrimerSemestre"
    ruta6 = "C:/proyecto-3-chiq/docs/inputs/programas.xlsx"

    # Usa el widget file_uploader para permitir la subida de archivos
    uploaded_file = st.file_uploader("Sube los archivos del SNIES para poder procesar los datos necesarios",
                                     type="xlsx")

    # Se van a leer todos los archivos de los 3 años anteriores
    primer_anio = 2020
    dict_df_admitidos: Dict[int, pd.DataFrame] = {}
    dict_df_graduados: Dict[int, pd.DataFrame] = {}
    dict_df_matriculados_primer_semestre: Dict[int, pd.DataFrame] = {}
    dict_df_inscritos: Dict[int, pd.DataFrame] = {}
    dict_df_matriculados: Dict[int, pd.DataFrame] = {}
    df_programas_academicos = pd.read_excel(ruta6)

    for i in range(1, 3):
        anio = primer_anio + i
        ruta_admitidos = ruta1 + f"{anio}.xlsx"
        print(ruta_admitidos)
        ruta_inscritos = ruta2 + f"{anio}.xlsx"
        ruta_graduados = ruta3 + f"{anio}.xlsx"
        ruta_matriculados = ruta4 + f"{anio}.xlsx"
        ruta_matriculados_primer_semestre = ruta5 + f"{anio}.xlsx"
        if i == 1:
            dict_df_admitidos[anio] = pd.read_excel(ruta_admitidos)
            dict_df_inscritos[anio] = pd.read_excel(ruta_inscritos)
        #dict_df_graduados[anio] = pd.read_excel(ruta_graduados)
        #dict_df_matriculados[anio] = pd.read_excel(ruta_matriculados)
        #dict_df_matriculados_primer_semestre[anio] = pd.read_excel(ruta_matriculados_primer_semestre)

    # Para temas de pruebas:
    """
    st.write(dict_df_admitidos[2021])
    st.write(dict_df_inscritos[2021])
    st.write(dict_df_graduados[2021])
    st.write(dict_df_matriculados[2021])
    st.write(dict_df_matriculados_primer_semestre[2021])
    st.write(df_programas_academicos)
    """

    # Chequea si un archivo ha sido subido
    if uploaded_file is not None:
        # Cargar y procesar el archivo Excel
        df = pd.read_excel(uploaded_file)
        st.write("Archivo cargado con éxito.")
        st.dataframe(df)
        st.write("Archivo cargado con éxito.")
        st.dataframe(df)  # Guarda el DataFrame en session_state
        st.session_state['df_cargado'] = df