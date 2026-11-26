import streamlit as st

st.title("Power Calculator")

base = st.number_input("Base", value=2.0)
exponent = st.number_input("Exponent", value=2.0)

if st.button("Calculate"):
    result = base ** exponent
    st.metric("Result", result)