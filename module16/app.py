import streamlit as st

def main ():
        st.title('Hello World')
        if st.button("Click me"):
            st.write('Button clicked')
        if st.checkbox('Check me'):
            st.text('')
        user_input = st.text_input("Enter text", "Sample text")
        st.write("you entered:", user_input)
        age = st.number_input('Enter your age',min_value=0,max_value=100)
        st.write(f"Your age is {age}")
        message = st.text_area('Enter your message')
        st.write(f"Your message is {message}")
        choice = st.radio("Pick one",["choice 1","choice 2","choice 3"])
        st.write(f"Your choice is {choice}")
        if st.button("Success"):
            st.success ("Opperation was successful")
        try:
            1/0
        except Exception as e:
            st.exception(e)

if __name__ == '__main__':
    main()