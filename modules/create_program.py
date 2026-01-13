import streamlit as st
import pandas as pd
from core.storage import save_excel, load_excel

def render():
    st.header("Create Program")

    with st.form("program_form"):
        program = st.text_input("Program Name")
        job_family = st.text_input("Job Family")
        start = st.date_input("Start Date")
        end = st.date_input("End Date")
        submit = st.form_submit_button("Save Program")

    if submit:
        df = load_excel("Programs_" + ".xlsx")
        new = pd.DataFrame([{
            "Program": program,
            "Job Family": job_family,
            "Start": start,
            "End": end
        }])
        df = pd.concat([df, new], ignore_index=True)
        save_excel(df, "Programs.xlsx")
        st.success("Program saved")
