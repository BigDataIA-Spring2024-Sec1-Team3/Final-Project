import streamlit as st

def login_page():
    with st.form("login_form", clear_on_submit=True):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            # Add your authentication logic here
            if username == "user" and password == "password":
                st.success("Logged in successfully!")
                st.write("Welcome, " + username + "!")
            else:
                st.error("Invalid username or password")
