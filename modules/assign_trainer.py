import streamlit as st
import pandas as pd
from core.storage import load_excel, save_excel
from core.assignment import match_trainer


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    return df


def render():
    st.header("Assign Trainers")

    trainers = load_excel("Trainer_SkillProgression.xlsx")
    if trainers.empty:
        st.warning("No trainer data available. Upload Trainer data first.")
        return

    uploaded = st.file_uploader("Upload Batch Calendar to Assign", type=["xlsx", "csv"])

    if not uploaded:
        st.info("Please upload a Batch Calendar file.")
        return

    # Load file
    if uploaded.name.endswith(".csv"):
        batch_df = pd.read_csv(uploaded)
    else:
        batch_df = pd.read_excel(uploaded, engine="openpyxl")

    # Normalize column names
    batch_df = normalize_columns(batch_df)

    # Map required columns
    col_map = {}

    for c in batch_df.columns:
        if "module" in c:
            col_map["module"] = c
        if "tech" in c or "technology" in c:
            col_map["tech"] = c
        if c in ["start", "start date"]:
            col_map["start"] = c
        if c in ["end", "end date"]:
            col_map["end"] = c

    missing = [k for k in ["module", "tech"] if k not in col_map]
    if missing:
        st.error(f"Missing required columns: {missing}. Found columns: {list(batch_df.columns)}")
        return

    # Create Trainer column
    batch_df["trainer"] = ""

    # Assign trainers
    for i, row in batch_df.iterrows():
        module_val = str(row[col_map["module"]])
        tech_val = str(row[col_map["tech"]])
        trainer = match_trainer(module_val, tech_val, trainers)
        batch_df.at[i, "trainer"] = trainer if trainer else ""

    st.subheader("Trainer Mapping Preview")
    edited = st.data_editor(batch_df, use_container_width=True)

    if st.button("Save Assignments"):
        save_excel(edited, "Assignments.xlsx")
        st.success("Assignments saved successfully.")
