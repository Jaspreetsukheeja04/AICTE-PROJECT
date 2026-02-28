import streamlit as st

st.title("AI Study Buddy - NLP Project")

text = st.text_area("Enter your text")

if st.button("Analyze Text"):
    if text:
        word_count = len(text.split())
        char_count = len(text)
        
        st.write("Word Count:", word_count)
        st.write("Character Count:", char_count)
        
        if "good" in text.lower():
            st.write("Basic Sentiment: Positive")
        elif "bad" in text.lower():
            st.write("Basic Sentiment: Negative")
        else:
            st.write("Basic Sentiment: Neutral")
    else:
        st.write("Please enter some text.")
