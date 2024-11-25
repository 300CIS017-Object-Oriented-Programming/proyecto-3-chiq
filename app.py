import streamlit as st
from pages import page1, cargar_datos2, filtrado_informacion3, procesamiento_datos4, visual5, calculo6

# Diccionario de páginas
pages = {
    "Página 1": page1,
    "Cargar Datos": cargar_datos2,
    "Filtrado de Información": filtrado_informacion3,
    "Procesamiento de Datos": procesamiento_datos4,
    "Visualización": visual5,
    "Calculo" : calculo6
}

# Barra de navegación
st.sidebar.title("Navegación")
selection = st.sidebar.radio("Ir a", list(pages.keys()))

# Mostrar la página seleccionada
page = pages[selection]
page.app()
