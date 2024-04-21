import streamlit as st

def signup_page():
    # new_username = st.text_input("Username")
    # new_password = st.text_input("Password", type="password")
    with st.form("signup_form", clear_on_submit=True):
        email = st.text_input("Email", key="register_email")
        password = st.text_input(
            "Password", type="password", key="register_password")
        password_confirm = st.text_input(
            "Confirm Password", type="password", key="register_password_confirm")
        submitted = st.form_submit_button("Signup")
        if submitted:
            st.success("Signup successful!")
            st.form_clear()
