import streamlit as st
import pandas as pd
from core.storage import save_excel, load_excel


def render():
    if not st.session_state.get("is_admin", False):
        st.warning("Admin access only. Please login as admin.")
        return

    st.header("Trainer Upload & Edit")

    file = st.file_uploader("Upload Trainer Progression Sheet", type=["xlsx"])

    if file:
        df = pd.read_excel(file, engine="openpyxl")
        st.dataframe(df, use_container_width=True)

        edited = st.data_editor(df, use_container_width=True)

        if st.button("Save Trainers"):
            save_excel(edited, "Trainer_SkillProgression.xlsx")
            st.success("Trainer data saved")

    else:
        df = load_excel("Trainer_SkillProgression.xlsx")
        if not df.empty:
            edited = st.data_editor(df, use_container_width=True)
            if st.button("Save Trainers"):
                save_excel(edited, "Trainer_SkillProgression.xlsx")
                st.success("Trainer data updated")
