"""
Streamlit Mini-App – sehr einfache Version
Lecture: Structure of Functions and Applications

Run with:
    streamlit run app.py
"""

import streamlit as st


# ------------------------------------------------------------
# Pure function (Business Logic)
# ------------------------------------------------------------
def multiply(number: float, factor: int) -> float:
    """Multiply a number by a given factor."""
    return number * factor


# ------------------------------------------------------------
# Streamlit App
# ------------------------------------------------------------
st.set_page_config(
    page_title="Simple Multiplier",
    page_icon="✖️",
    layout="centered"
)

st.title("Simple Multiplier")
st.markdown("Enter a number, choose a factor, and see the result.")

# --- Input ---
number = st.number_input("Your number", value=5.0, step=1.0)

# --- Dropdown ---
factor = st.selectbox(
    "Multiply by",
    options=[2, 3, 4, 5, 6, 7, 8, 9, 10],
    index=0,  # default = 2 (double)
    format_func=lambda x: f"× {x}"
)

# --- Result ---
result = multiply(number, factor)

st.markdown("---")
st.metric(label="Result", value=result)

# --- Footer ---
st.markdown("---")
st.caption(
    "Lecture: Structure of Functions and Applications  •  "
    "efl – the Data Science Institute"
)
