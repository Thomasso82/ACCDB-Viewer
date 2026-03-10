import pandas as pd
from sqlalchemy import create_engine
import os


def get_postgres_url() -> str:
    # Můžeš nahradit natvrdo, nebo použít env proměnnou
    return os.getenv(
        "POSTGRES_URL",
        "postgresql+psycopg2://user:password@localhost:5432/moje_db",
    )


def migrate_table_to_postgres(df: pd.DataFrame, table_name: str):
    try:
        engine = create_engine(get_postgres_url())
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        return True, f"Tabulka '{table_name}' byla úspěšně migrována do PostgreSQL."
    except Exception as e:
        return False, f"Chyba při migraci: {e}"
