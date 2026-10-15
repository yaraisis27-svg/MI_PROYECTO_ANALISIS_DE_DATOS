import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("YARDAS_PASOS_DATOS_TICS.xlsx", index_col=0)


st.dataframe(df.head())

st.header("Estadística descriptiva")
st.dataframe(df.describe())



df.columns = [c.lower().replace(' ', '_') for c in df.columns]


col1, col2 = st.columns(2)

with col1 :
    fig, ax = plt.subplots()
    ax.boxplot(df['pases_completos'])
    st.header("Diagrama de caja y bigote\nde pases completos")
    st.pyplot(fig)



with col2:
    fig, ax = plt.subplots()
    ax.boxplot(df["yardas_totales"])
    st.header("Diagrama de caja y bigote\nde yardas totales")
    st.pyplot(fig)