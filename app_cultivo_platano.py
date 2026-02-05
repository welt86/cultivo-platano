import streamlit as st

st.set_page_config(page_title="Cultivo de Plátano", layout="wide")

st.title("🌱 Sistema Técnico para el Cultivo de Plátano")
st.write("Aplicación técnica basada en literatura agroindustrial colombiana.")

tabs = st.tabs([
    "Descripción",
    "Clima",
    "Siembra",
    "Alta Densidad",
    "Fertilización",
    "Enfermedades",
    "Mantenimiento",
    "Cosecha"
])

# 1. DESCRIPCIÓN
with tabs[0]:
    st.header("Descripción del Cultivo")
    st.write("""
    El plátano es un cultivo de gran importancia económica y social en Colombia.
    Su manejo técnico adecuado permite incrementar significativamente la productividad
    y la rentabilidad, especialmente mediante nuevas tecnologías como la siembra
    en altas densidades.
    """)

# 2. CLIMA
with tabs[1]:
    st.header("Requerimientos Climáticos")

    st.write("**Temperatura:**")
    st.write("Óptima entre 26 y 30 °C. El cultivo no tolera heladas.")

    st.write("**Precipitación:**")
    st.write("Ideal entre 1800 y 2500 mm anuales, bien distribuidos.")

    st.write("**Altitud:**")
    st.write("Desde nivel del mar hasta 1800 msnm.")

    st.write("**Humedad relativa:**")
    st.write("Alta, superior al 75 %.")

# 3. SIEMBRA
with tabs[2]:
    st.header("Sistemas de Siembra")

    st.write("**Siembra tradicional:**")
    st.write("Distancias comunes de 3 x 3 m o 4 x 4 m, una planta por sitio.")

    st.write("**Preparación del suelo:**")
    st.write("""
    - Suelos profundos y bien drenados  
    - Labranza mínima  
    - Corrección de pH si es necesario
    """)

# 4. ALTA DENSIDAD
with tabs[3]:
    st.header("Siembra en Altas Densidades")

    st.write("""
    Basada en investigaciones del Dr. Sylvio Belalcázar, la siembra en altas densidades
    permite incrementos de producción superiores al 100 %.
    """)

    st.write("**Densidades comunes:**")
    st.write("""
    - 2500 plantas/ha (2 x 2 m)
    - 3332 plantas/ha (3 x 2 m, dos plantas por sitio)
    - 4998 plantas/ha (tres plantas por sitio)
    """)

    st.write("**Ventajas:**")
    st.write("""
    - Mayor rendimiento por hectárea  
    - Menor incidencia de Sigatoka  
    - Mejor aprovechamiento del suelo
    """)

# 5. FERTILIZACIÓN
with tabs[4]:
    st.header("Fertilización y Nutrición")

    st.write("""
    El plátano es altamente demandante de nutrientes, especialmente:
    """)

    st.write("""
    - Nitrógeno (N): desarrollo vegetativo  
    - Fósforo (P): raíces y floración  
    - Potasio (K): llenado de racimos
    """)

    st.write("La fertilización debe ajustarse según análisis de suelo y etapa del cultivo.")

# 6. ENFERMEDADES
with tabs[5]:
    st.header("Enfermedades y Plagas")

    st.write("**Principales enfermedades:**")
    st.write("""
    - Sigatoka negra  
    - Sigatoka amarilla  
    - Moko del plátano
    """)

    st.write("**Manejo:**")
    st.write("""
    - Buen drenaje  
    - Control de humedad  
    - Eliminación de material infectado  
    - Manejo integrado
    """)

# 7. MANTENIMIENTO
with tabs[6]:
    st.header("Mantenimiento del Cultivo")

    st.write("""
    - Deshije controlado  
    - Control de malezas  
    - Deshoje sanitario  
    - Tutoramiento en altas densidades
    """)

# 8. COSECHA
with tabs[7]:
    st.header("Cosecha")

    st.write("""
    La cosecha se realiza entre 14 y 20 meses según densidad y condiciones.
    El peso del racimo puede variar entre 14 y 20 kg.
    """)

    st.write("La recolección debe hacerse de forma escalonada para mejorar la comercialización.")

