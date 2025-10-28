import streamlit as st

st.sidebar.header("Sidebar")
st.sidebar.write("this is the side bar")
st.sidebar.selectbox("Choose an option",["option1","option2","option3"])
st.sidebar.radio("Go to",["home","Data","settings"])