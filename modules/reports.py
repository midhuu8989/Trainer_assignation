import streamlit as st
import pandas as pd
import plotly.express as px
from core.storage import load_excel

def render():
    st.header("Reports & Gantt")

    assignments = load_excel("Assignments.xlsx")
    if assignments.empty:
        st.info("No assignments yet.")
        return

    assignments["Start"] = pd.to_datetime(assignments["Start"])
    assignments["End"] = pd.to_datetime(assignments["End"])

    fig = px.timeline(
        assignments,
        x_start="Start",
        x_end="End",
        y="Trainer",
        color="Module",
        hover_data=["Tech"]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(assignments, use_container_width=True)
