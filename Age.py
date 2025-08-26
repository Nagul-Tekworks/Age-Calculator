import streamlit as st
from datetime import date

# Title
st.title("🎉 Age Calculator App")

# Date input with min & max values
birth_date = st.date_input(
    "Select your date of birth:",
    min_value=date(1900, 1, 1),   # earliest allowed date
    max_value=date.today()        # today's date as the latest
)

# Button to calculate
if st.button("Calculate Age"):
    today = date.today()
    age = today.year - birth_date.year

    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    st.success(f"✨ Your age is: {age} years")
