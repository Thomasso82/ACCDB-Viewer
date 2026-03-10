import streamlit as st


def setup_page_config():
    st.set_page_config(
        page_title="ACCDB Viewer & Migrator",
        layout="wide",
    )


def render_header():
    st.title("ACCDB Viewer & Migrator")
    st.caption("Načítání, prohlížení a migrace Microsoft Access databází (.accdb)")
