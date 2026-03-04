import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EduTrack Pro", layout="wide")

API_URL = "http://127.0.0.1:5000"

st.markdown("""
<style>
.stApp {
    background-color: #ffffff;
}

[data-testid="stVerticalBlock"] > div:has(.login-box) {
    background: #ffffff;
    padding: 40px;
    border-radius: 24px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    border: 1px solid #f0f0f0;
    width: 450px;
    margin: 0 auto;
}

.login-header {
    color: #000000 !important;
    font-size: 30px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 20px;
}

.stMarkdown p, label {
    color: #000000 !important;
    font-weight: 600;
}

.stTextInput > div > div > input {
    background-color: #f7f7f7 !important;
    color: #000 !important;
    border-radius: 12px !important;
    border: 1px solid #eee !important;
}

.stButton > button {
    background-color: #000000 !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    width: 100% !important;
    height: 50px !important;
    font-weight: 700 !important;
    border: none !important;
}

[data-testid="stSidebar"] {
    background-color: #000000 !important;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

div[role="radiogroup"] > label > div:first-child {
    display: none !important;
}

div[role="radiogroup"] > label {
    padding: 15px 20px !important;
    border-radius: 12px !important;
    margin-bottom: 8px !important;
    transition: 0.3s;
}

div[role="radiogroup"] > label:hover {
    background-color: #222222 !important;
}

div[role="radiogroup"] > label[data-checked="true"] {
    background-color: #ffffff !important;
}

div[role="radiogroup"] > label[data-checked="true"] p {
    color: #000000 !important;
    font-weight: 800 !important;
}

.metric-box {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
}
.m-blue { background-color: #007bff; color: white !important; }
.m-green { background-color: #28a745; color: white !important; }
.m-orange { background-color: #fd7e14; color: white !important; }

.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #000;
}

.success-btn > div > button {
    background-color: #28a745 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

if "token" not in st.session_state:
    st.session_state.token = None
if "page" not in st.session_state:
    st.session_state.page = "login"
if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"


def login_page():
    st.write("<div style='height: 80px;'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        st.markdown("<div class='login-header'>Sign in</div>", unsafe_allow_html=True)
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        st.write("")
        if st.button("Get Started"):
            response = requests.post(f"{API_URL}/login", json={"username": email, "password": password})
            if response.status_code == 200:
                st.session_state.token = response.json()["token"]
                st.rerun()
            else:
                st.error("Invalid credentials")
        if st.button("Create new account"):
            st.session_state.page = "register"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


def register_page():
    st.write("<div style='height: 80px;'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        st.markdown("<div class='login-header'>Create Account</div>", unsafe_allow_html=True)
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        st.write("")
        if st.button("Sign Up"):
            response = requests.post(f"{API_URL}/register", json={"username": email, "password": password})
            if response.status_code == 200:
                st.session_state.page = "login"
                st.rerun()
        if st.button("Back to Login"):
            st.session_state.page = "login"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


def main_app():
    st.sidebar.markdown("<h1 style='text-align:center;'>EduTrack</h1>", unsafe_allow_html=True)
    st.sidebar.write("---")

    options = ["Dashboard", "Add Grade"]
    idx = options.index(st.session_state.menu)
    st.session_state.menu = st.sidebar.radio("NAV", options, index=idx)

    st.sidebar.markdown("<div style='height: 40vh;'></div>", unsafe_allow_html=True)
    if st.sidebar.button("Logout"):
        st.session_state.token = None
        st.session_state.page = "login"
        st.rerun()

    headers = {"Authorization": st.session_state.token}

    if st.session_state.menu == "Dashboard":
        st.markdown("<div class='main-title'>Academic Dashboard</div>", unsafe_allow_html=True)
        response = requests.get(f"{API_URL}/grades", headers=headers)
        if response.status_code == 200:
            grades = response.json().get("grades", [])
            if grades:
                df = pd.DataFrame(grades)
                df["grade"] = pd.to_numeric(df["grade"])
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.markdown(f"<div class='metric-box m-blue'>Average<br><h2>{df['grade'].mean():.2f}</h2></div>",
                                unsafe_allow_html=True)
                with c2:
                    st.markdown(f"<div class='metric-box m-green'>Highest<br><h2>{df['grade'].max()}</h2></div>",
                                unsafe_allow_html=True)
                with c3:
                    st.markdown(f"<div class='metric-box m-orange'>Lowest<br><h2>{df['grade'].min()}</h2></div>",
                                unsafe_allow_html=True)
                st.write("")
                st.dataframe(df, use_container_width=True)
                st.bar_chart(df.set_index("subject")["grade"], color="#000000")
            else:
                st.info("No grades added yet.")

    elif st.session_state.menu == "Add Grade":
        st.markdown("<div class='main-title'>Add New Grade</div>", unsafe_allow_html=True)
        subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "English", "History", "Other"]
        sel = st.selectbox("Subject", subjects)
        name = st.text_input("Custom Name") if sel == "Other" else sel
        val = st.number_input("Grade", 1, 10, 5)

        if st.button("Save Grade"):
            res = requests.post(f"{API_URL}/add-grade", headers=headers, json={"subject": name, "grade": val})
            if res.status_code == 200:
                st.markdown("<div class='success-btn'>", unsafe_allow_html=True)
                if st.button("✅ Grade Saved! Click here to go to Dashboard"):
                    st.session_state.menu = "Dashboard"
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.error("Error saving grade.")


if st.session_state.token is None:
    if st.session_state.page == "login":
        login_page()
    else:
        register_page()
else:
    main_app()