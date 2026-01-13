import streamlit as st
import os
from modules import (
    overview, create_program, batch_upload,
    trainer_admin, users, assign_trainer, reports, export
)
from core.config import get_current_quarter


# ------------------- Page Config -------------------
st.set_page_config(
    page_title="Career Shaper™ – Trainer Loading & Utilization",
    page_icon="📊",
    layout="wide",
)


# ------------------- Styles -------------------
st.markdown("""
<style>
.header {
    background: linear-gradient(90deg, #006BB6, #00A5A5);
    padding: 14px 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
}
.sidebar-btn {
    padding: 10px;
    margin: 4px 0;
    border-radius: 8px;
    background: #FFFFFF;
    cursor: pointer;
    border: 1px solid #E0E0E0;
}
.sidebar-btn:hover {
    background: #E6F3FF;
}
.sidebar-btn.active {
    background: #006BB6;
    color: white;
    border-color: #006BB6;
}
</style>
""", unsafe_allow_html=True)


# ------------------- Session Defaults -------------------
if "page" not in st.session_state:
    st.session_state.page = "Overview"

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False


# ------------------- Login -------------------
def login():
    st.sidebar.markdown("### 🔐 Login")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username == "admin" and password == "admin@123":
            st.session_state.is_admin = True
            st.sidebar.success("Logged in as Admin")
        else:
            st.sidebar.error("Invalid credentials")


login()


# ------------------- Header -------------------
with st.container():
    st.markdown('<div class="header">', unsafe_allow_html=True)
    left, right = st.columns([1, 4])

    with left:
        logo = "./assets/hcl_careershaper_logo.png"
        if os.path.exists(logo):
            st.image(logo, use_container_width=True)
        else:
            st.markdown("**Career Shaper™**")

    with right:
        st.markdown("## Career Shaper™ – Trainer Loading & Utilization")
        st.markdown("HCLTech EdTech | Trainer Loading & Assessment Management")

    st.markdown('</div>', unsafe_allow_html=True)


# ------------------- Navigation -------------------
base_pages = [
    "Overview",
    "Create Program",
    "Batch Calendar Upload",
    "User Details Upload",
    "Assign Trainer",
    "Reports & Gantt",
    "Export Loading Sheet"
]

if st.session_state.is_admin:
    base_pages.insert(3, "Trainer Upload & Edit")


with st.sidebar:
    st.markdown("### 📌 Navigation")
    for p in base_pages:
        if st.button(p, key=p):
            st.session_state.page = p


# ------------------- Page Router -------------------
page = st.session_state.page

if page == "Overview":
    overview.render()

elif page == "Create Program":
    create_program.render()

elif page == "Batch Calendar Upload":
    batch_upload.render()

elif page == "Trainer Upload & Edit":
    trainer_admin.render()

elif page == "User Details Upload":
    users.render()

elif page == "Assign Trainer":
    assign_trainer.render()

elif page == "Reports & Gantt":
    reports.render()

elif page == "Export Loading Sheet":
    export.render()
