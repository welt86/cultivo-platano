import streamlit as st

st.set_page_config(page_title="Cultivo de Plátano", layout="wide")

st.title("🌱 App Básica para Cultivo de Plátano")

tabs = st.tabs(["Información del Cultivo", "Métodos de Siembra"])

with tabs[0]:
    st.header("Información General")
    area = st.number_input("Área del terreno (hectáreas)", min_value=0.1, step=0.1)

    if area:
        st.write(f"Siembra 4 x 4: {int((area * 10000) / 16)} plantas")
        st.write(f"Siembra 3 x 3: {int((area * 10000) / 9)} plantas")

with tabs[1]:
    st.header("Métodos de Siembra")
    st.write("3 x 3: Triángulo")
    st.write("4 x 4: Filas")

