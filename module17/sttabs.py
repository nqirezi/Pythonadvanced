import streamlit as st

tab1,tab2, tab3 = st.tabs(["Tab1","Tab2","Tab3"])

with tab1:
    st.header("Content for tab 1 ")
    st.write("This is the content of first tab")

with tab2:
    st.header("Content for tab 2")
    st.write("This is the content of second tab")

with tab3:
    st.header("Content for tab 3")
    st.write("This is the content of third tab")