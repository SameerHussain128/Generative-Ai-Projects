# -*- coding: utf-8 -*-
"""Sameer GPT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KAO-WSjWzEzRSm0iNyYWrE8UTJ7jDuQW
"""

# !pip install langchain-openai
# !pip install streamlit

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
#from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = "enter key here"

# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "enter key here"

# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","I am a chatbot. I am here to assist you. Please type your queries"),
        ("user","Question:{question}")
    ]
)

# Streamlit framework

st.title("LLM OPENAI PROJECT")
# Subheader for the author's name
#st.subheader("Developed by : Mohd Sameer Hussain")
# Custom markdown for a smaller header
st.markdown("<h3 style='font-size: 23px;'>Developed by : Mohd Sameer Hussain</h3>", unsafe_allow_html=True)

# Input field with increased font size
input_text = st.text_input("Write your question here", placeholder="Type your question here...", 
                            label_visibility="collapsed")
# OpenAI LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo")
#llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
  st.write(chain.invoke({"question":input_text}))