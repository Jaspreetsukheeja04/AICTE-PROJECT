import streamlit as st
from collections import Counter

st.title("AI Study Buddy for Bionformatics")

st.sidebar.title("About")
st.sidebar.write("This app performs basic NLP analysis including word count, sentence count, keyword extraction and sentiment detection.")

text = st.text_area("Enter your text")

if st.button("Analyze Text"):
    if text:
        words = text.split()
        sentences = text.split(".")
        
        word_count = len(words)
        sentence_count = len([s for s in sentences if s.strip() != ""])
        
        word_freq = Counter(words)
        common_words = word_freq.most_common(5)

        st.subheader("Text Statistics")
        st.write("Word Count:", word_count)
        st.write("Sentence Count:", sentence_count)

        st.subheader("Top 5 Frequent Words")
        st.write(common_words)

        if "good" in text.lower():
            st.write("Sentiment: Positive")
        elif "bad" in text.lower():
            st.write("Sentiment: Negative")
        else:
            st.write("Sentiment: Neutral")
    else:
        st.write("Please enter some text.")
