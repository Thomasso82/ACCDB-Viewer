import pandas as pd


def fulltext_search(df: pd.DataFrame, query: str) -> pd.DataFrame:
    if not query:
        return df
    query_lower = query.lower()
    mask = df.apply(
        lambda row: row.astype(str).str.lower().str.contains(query_lower, na=False).any(),
        axis=1,
    )
    return df[mask]
