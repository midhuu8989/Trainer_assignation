import streamlit as st
from core.storage import quarter_path
import os

def render():
    st.header("Export Loading Sheet")

    path = quarter_path()
    files = os.listdir(path)

    for f in files:
        full = os.path.join(path, f)
        with open(full, "rb") as fp:
            st.download_button(
                f"Download {f}",
                fp,
                file_name=f,
                use_container_width=True
            )
