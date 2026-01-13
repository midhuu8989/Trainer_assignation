import streamlit as st
import pandas as pd
from core.storage import save_excel, load_excel

def render():
    st.header("User Details Upload")

    file = st.file_uploader("Upload User Role Mapping", type=["xlsx", "csv"])

    if file:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file, engine="openpyxl")

        st.dataframe(df, use_container_width=True)

        if st.button("Save Users"):
            save_excel(df, "Users.xlsx")
            st.success("Users saved")

    else:
        df = load_excel("Users.xlsx")
        if not df.empty:
            edited = st.data_editor(df, use_container_width=True)
            if st.button("Save Users"):
                save_excel(edited, "Users.xlsx")
                st.success("Users updated")
