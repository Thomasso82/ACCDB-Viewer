import pandas as pd
import streamlit as st


def render_table_view(df: pd.DataFrame, table_name: str):
    st.subheader(f"Tabulka: {table_name}")
    st.dataframe(df)

    st.download_button(
        label="Stáhnout jako CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=f"{table_name}.csv",
        mime="text/csv",
    )
