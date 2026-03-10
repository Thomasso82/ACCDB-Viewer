import pandas as pd
import pyodbc


def load_access_file(uploaded_file):
    # U tebe může být i pevná cesta, tohle je placeholder
    conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        rf"DBQ={uploaded_file.name};"
    )
    # V produkci: uložit do temp souboru a použít jeho cestu
    conn = pyodbc.connect(conn_str)
    return conn


def list_tables(conn):
    cursor = conn.cursor()
    tables = []
    for row in cursor.tables(tableType="TABLE"):
        tables.append(row.table_name)
    return tables


def load_table_data(conn, table_name: str) -> pd.DataFrame:
    query = f"SELECT * FROM [{table_name}]"
    df = pd.read_sql(query, conn)
    return df
