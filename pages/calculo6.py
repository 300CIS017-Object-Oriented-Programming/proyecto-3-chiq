import streamlit as st
import pandas as pd
import os

def app():
    st.title("Cálculo de Estadísticas por Programa y Año")
    if 'df_cargado' in st.session_state:
        df = st.session_state['df_cargado']
    #con data frame
    #Cálculo de estudiantes inscritos por programa y año.
    #Cálculo de estudiantes admitidos por programa y año.
    #Cálculo de nuevos estudiantes matriculados por programa y año.
    #Cálculo del total de estudiantes matriculados por programa y año.
    #Cálculo de estudiantes graduados por programa y año.

    else:
            st.warning("No se cargaron datos.")
