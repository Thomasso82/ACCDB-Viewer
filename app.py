import streamlit as st
import pyodbc
import pandas as pd
import os

st.set_page_config(page_title="ACCDB Viewer", layout="wide")

st.title("📁 Access Database Viewer (ACCDB → Streamlit)")

# --- Výběr souboru ---
uploaded_file = st.file_uploader("Nahraj ACCDB soubor", type=["accdb", "mdb"])

if uploaded_file:
    # Uložení do dočasného souboru
    temp_path = "temp.accdb"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Soubor nahrán. Připojuji se k databázi...")

    # --- Připojení k databázi ---
    conn_str = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        rf"DBQ={os.path.abspath(temp_path)};"
    )

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # --- Načtení seznamu tabulek ---
        tables = [t.table_name for t in cursor.tables(tableType="TABLE")]

        st.subheader("📋 Tabulky v databázi")
        selected_table = st.selectbox("Vyber tabulku", tables)

        if selected_table:
            query = f"SELECT * FROM [{selected_table}]"
            df = pd.read_sql(query, conn)

            st.subheader(f"📄 Náhled tabulky: {selected_table}")
            st.dataframe(df, use_container_width=True)

            # --- Export do CSV ---
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Exportovat do CSV",
                data=csv,
                file_name=f"{selected_table}.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"Chyba při načítání databáze: {e}")
