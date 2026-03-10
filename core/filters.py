import pandas as pd


def apply_filters(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    if not filters:
        return df

    filtered = df.copy()
    for col, value in filters.items():
        if value is None or value == "":
            continue
        filtered = filtered[filtered[col].astype(str) == str(value)]
    return filtered
