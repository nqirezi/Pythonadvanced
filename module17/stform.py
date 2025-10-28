import streamlit as st

with st.form("my_form",clear_on_submit=True):
    name = st.text_input("Name")
    age = st.slider("Age")
    email = st.text_input("Email")
    biography = st.text_area("Short Bio")
    terms = st.checkbox("I agree to terms and conditions")
    subit_button = st.form_submit_button(label="Submit")


if subit_button:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Email: {email}")
    st.write(f"Biography: {biography}")
    if terms:
        st.write("you agreed to the terms and conditions")
    else:
        st.write("you did not  agreed to the terms and conditions")
