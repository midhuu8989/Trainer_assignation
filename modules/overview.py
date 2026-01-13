import streamlit as st
import pandas as pd
from core.storage import load_excel

def render():
    st.header("Overview")

    programs = load_excel("Programs.xlsx")
    batches = load_excel("Batches.xlsx")
    trainers = load_excel("Trainer_SkillProgression.xlsx")
    assignments = load_excel("Assignments.xlsx")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Programs", len(programs))
    col2.metric("Batches", len(batches))
    col3.metric("Trainers", len(trainers))
    col4.metric("Assignments", len(assignments))

    st.subheader("Programs")
    if programs.empty:
        st.info("No programs created yet.")
    else:
        st.dataframe(programs, use_container_width=True)

    st.subheader("Trainer Assignments")
    if assignments.empty:
        st.info("No assignments yet.")
    else:
        st.dataframe(assignments, use_container_width=True)
