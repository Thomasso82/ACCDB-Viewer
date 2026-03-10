import streamlit as st
from typing import Tuple, Dict, Any


def render_sidebar() -> Tuple[Any, str, str, Dict[str, Any], bool]:
    st.sidebar.subheader("Vstupní data")
    accdb_file = st.sidebar.file_uploader("Nahraj .accdb soubor", type=["accdb"])

    selected_table = st.sidebar.text_input("Název tabulky (zatím ručně)")

    st.sidebar.subheader("Vyhledávání")
    search_query = st.sidebar.text_input("Fulltext dotaz")

    # Jednoduché placeholder filtry – můžeš později nahradit dynamickými
    filters = {}

    st.sidebar.subheader("Migrace")
    migrate_btn = st.sidebar.button("Migrovat do PostgreSQL")

    return accdb_file, selected_table, search_query, filters, migrate_btn
