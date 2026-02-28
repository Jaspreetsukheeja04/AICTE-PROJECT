import streamlit as st
from textblob import TextBlob
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

st.title("AI Study Buddy - NLP Project")

text = st.text_area("Enter your text")

if st.button("Analyze Text"):
    if text:
        analysis = TextBlob(text)
        st.write("Sentiment Polarity:", analysis.sentiment.polarity)
        st.write("Sentiment Subjectivity:", analysis.sentiment.subjectivity)
    else:
        st.write("Please enter some text.")
