import streamlit as st
from datetime import date

# Title
st.title("🎉 Age Calculator App")

# Input - Date picker for birthdate
birth_date = st.date_input("Select your date of birth:")

# Button to calculate
if st.button("Calculate Age"):
    today = date.today()
    age = today.year - birth_date.year

    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    st.success(f"✨ Your age is: {age} years")
