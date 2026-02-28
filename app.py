import streamlit as st

st.title("AI Study Buddy - NLP Project")

user_input = st.text_area("Enter your text")

if st.button("Process"):
    st.write("You entered:")
    st.write(user_input)
