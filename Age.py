import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Age Calculator", page_icon="🎉", layout="centered")

# Title
st.title("🎉 Advanced Age Calculator")

# Start Date (Birthdate)
birth_date = st.date_input(
    "Select your Date of Birth:",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    format="DD-MM-YYYY"   # 👈 date format
)

# End Date (default = today)
end_date = st.date_input(
    "Select End Date (default: Today):",
    value=date.today(),
    min_value=birth_date,
    max_value=date.today(),
    format="DD-MM-YYYY"
)

# Button
if st.button("Calculate Age"):
    if end_date < birth_date:
        st.error("⚠️ End date must be after birth date!")
    else:
        diff = relativedelta(end_date, birth_date)
        years, months, days = diff.years, diff.months, diff.days

        st.success(
            f"✨ Your age is: **{years} years, {months} months, {days} days**"
        )
