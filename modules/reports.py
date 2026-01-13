import streamlit as st
import pandas as pd
from core.storage import load_excel

try:
    import plotly.express as px
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False


def render():
    st.header("Reports & Gantt")

    if not HAS_PLOTLY:
        st.error("Plotly is not installed. Please install plotly to view Gantt charts.")
        return

    assignments = load_excel("Assignments.xlsx")
    if assignments.empty:
        st.info("No assignments yet.")
        return

    assignments["Start"] = pd.to_datetime(assignments["Start"], errors="coerce")
    assignments["End"] = pd.to_datetime(assignments["End"], errors="coerce")

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
