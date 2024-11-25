import streamlit as st
import pandas as pd
import plotly.express as px
import re

# Configuración de la aplicación
def app():
    st.title("Análisis de Tendencias Históricas y Comparaciones")

    # Carga de múltiples archivos
    uploaded_files = st.file_uploader("Sube tus archivos Excel", type=["xlsx"], accept_multiple_files=True)

    if uploaded_files:
        data_frames = []

        # Procesar cada archivo
        for uploaded_file in uploaded_files:
            # Extraer el año del nombre del archivo
            file_name = uploaded_file.name
            year_match = re.search(r"\d{4}", file_name)
            year = int(year_match.group(0)) if year_match else None

            if year:
                # Leer el archivo
                df = pd.read_excel(uploaded_file)
                df["Año"] = year  # Agregar el año como columna
                data_frames.append(df)
            else:
                st.warning(f"No se encontró un año en el archivo: {file_name}")

        # Combinar todos los DataFrames en uno solo
        if data_frames:
            combined_df = pd.concat(data_frames, ignore_index=True)
            st.write("Datos combinados:")
            st.dataframe(combined_df)

            # Filtrar rango de años
            min_year, max_year = st.select_slider(
                "Selecciona el rango de años",
                options=sorted(combined_df["Año"].unique()),
                value=(combined_df["Año"].min(), combined_df["Año"].max())
            )
            filtered_df = combined_df[
                (combined_df["Año"] >= min_year) & (combined_df["Año"] <= max_year)
                ]

           # Página: Gráfico de líneas
            st.title("Gráfica de Tendencias Históricas")
            requerimientoC = st.selectbox("Selecciona el requerimiento: ", ["INSCRITOS", "ADMITIDOS", "Neos", "MATRICULADOS", "GRADUADOS"])
            graficoLinea = px.line( filtered_df, x="Año", y=requerimientoC, title="Tendencias Históricas por Año", labels={"value": "Cantidad", "variable": requerimientoC}, template="plotly_white" )
            graficoLinea.update_layout(hovermode="x unified")
            st.plotly_chart(graficoLinea, use_container_width=True)

            # Página: Gráfico de barras comparativo
            st.title("Gráficos Comparativos entre Programas")
            opcionGraficoComparativo = st.selectbox(
                "Selecciona la categoría de comparación:",
                ["Virtual/Presencial", "Género", "Nivel de Formación"]
            )
            requerimiento = st.selectbox("Selecciona el requerimiento: ", ["INSCRITOS", "ADMITIDOS", "Neos", "MATRICULADOS", "GRADUADOS"])


            graficoBarras = px.bar(
                filtered_df,
                x=opcionGraficoComparativo,
                y=requerimiento,
                color="Año",
                barmode="group",
                title=f"Comparativa por {opcionGraficoComparativo} ({min_year} - {max_year})",
                labels={"value": "Cantidad", "variable": requerimiento},
                template="plotly_white"
            )
            st.plotly_chart(graficoBarras, use_container_width=True)

        else:
            st.warning("No se pudieron combinar los archivos. Verifica los datos.")
    else:
        st.info("Por favor sube los archivos Excel para comenzar.")
