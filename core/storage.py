import os
import pandas as pd
from core.config import BASE_DATA_PATH, get_current_quarter


def quarter_path() -> str:
    q = get_current_quarter()
    path = os.path.join(BASE_DATA_PATH, q)
    os.makedirs(path, exist_ok=True)
    return path


def excel_path(name: str) -> str:
    return os.path.join(quarter_path(), name)


def save_excel(df: pd.DataFrame, filename: str):
    path = excel_path(filename)

    tmp = path.replace(".xlsx", "_tmp.xlsx")
    df.to_excel(tmp, index=False, engine="openpyxl")
    os.replace(tmp, path)

def load_excel(filename: str, columns=None) -> pd.DataFrame:
    path = excel_path(filename)
    if not os.path.exists(path):
        return pd.DataFrame(columns=columns)

    try:
        return pd.read_excel(path, engine="openpyxl")
    except ImportError:
        import streamlit as st
        st.error("Missing dependency: openpyxl. Please install it.")
        return pd.DataFrame(columns=columns)
    except Exception as e:
        import streamlit as st
        st.error(f"Error reading {filename}: {e}")
        return pd.DataFrame(columns=columns)

