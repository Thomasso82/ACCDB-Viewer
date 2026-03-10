import pandas as pd
import streamlit as st


def render_basic_charts(df: pd.DataFrame, table_name: str):
    st.subheader(f"Základní přehled – {table_name}")

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    if not numeric_cols:
        st.info("Žádné číselné sloupce pro grafy.")
        return

    col = st.selectbox("Vyber číselný sloupec pro graf:", numeric_cols)
    st.bar_chart(df[col])
