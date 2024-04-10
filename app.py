import streamlit as st
import pickle
import time
import os 

st.title("HealthAI Predictive Suite")
# with st.sidebar:
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/breast_cancer_prediction.py", label="Page 1", icon="1️⃣")
# st.page_link("pages/diabetes_prediction.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")

