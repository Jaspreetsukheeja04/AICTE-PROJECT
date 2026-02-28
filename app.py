import streamlit as st
from transformers import pipeline

st.title("AI Study Buddy - NLP Project")

qa_pipeline = pipeline("question-answering")

context = """
Structural bioinformatics is a branch of bioinformatics
that focuses on analyzing and predicting the 3D structure
of biological macromolecules like proteins and nucleic acids.
"""

question = st.text_area("Enter your question")

if st.button("Generate Answer"):
    result = qa_pipeline(question=question, context=context)
    st.write("Answer:", result["answer"])
