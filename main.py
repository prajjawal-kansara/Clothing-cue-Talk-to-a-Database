import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Clothing Cue: Talk to a Database")

question = st.text_input("Question: ")
enter_button = st.button("Ask a Question")

if enter_button and question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)
    
    st.header("Answer")
    st.write(response)

