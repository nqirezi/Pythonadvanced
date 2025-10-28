import streamlit as st

with st.container(border=True):
    st.header("This is a container")
    st.write("This is inside the container.")

st.write("This is outside the container.")