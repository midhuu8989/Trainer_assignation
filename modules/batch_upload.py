import streamlit as st
import pandas as pd
from core.storage import save_excel, load_excel

REQUIRED_COLS = ["Module", "Tech", "Hours", "Start", "End"]

def render():
    st.header("Batch Calendar Upload")

    program = st.text_input("Program Name")
    batch = st.text_input("Batch Name")

    file = st.file_uploader("Upload Batch Calendar", type=["xlsx", "csv"])

    if file:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file, engine="openpyxl")

        missing = [c for c in REQUIRED_COLS if c not in df.columns]
        if missing:
            st.error(f"Missing columns: {missing}")
            return

        st.dataframe(df, use_container_width=True)

        if st.button("Save Batch Calendar"):
            fname = f"BatchCalendar_{program}_{batch}.xlsx"
            save_excel(df, fname)
            st.success("Batch calendar saved")
