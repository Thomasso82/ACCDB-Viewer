import tempfile
import shutil
import pyodbc
import pandas as pd


def load_access_file(uploaded_file):
    """
    Uloží nahraný .accdb soubor do dočasného souboru,
    protože Access ODBC driver neumí pracovat se streamem.
    """
    # vytvoříme temp soubor s příponou .accdb
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".accdb")

    # zkopírujeme obsah uploadu do temp souboru
    shutil.copyfileobj(uploaded_file, temp)
    temp.close()

    # připojení k Access databázi
    conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        rf"DBQ={temp.name};"
    )

    conn = pyodbc.connect(conn_str)
    return conn


def list_tables(conn):
    """
    Vrátí seznam všech tabulek kromě systémových MSys*.
    Zahrnuje TABLE, VIEW, LINKED TABLES, QUERIES.
    """
    cursor = conn.cursor()
    tables = []

    for row in cursor.tables():
        name = row.table_name

        # přeskočíme systémové tabulky
        if name.startswith("MSys"):
            continue

        tables.append(name)

    return tables


def load_table_data(conn, table_name: str) -> pd.DataFrame:
    """
    Načte celou tabulku z Accessu.
    Používá TOP hack, aby obešel limity některých ODBC driverů.
    """
    query = f"SELECT TOP 1000000000 * FROM [{table_name}]"
    df = pd.read_sql(query, conn)
    return df
