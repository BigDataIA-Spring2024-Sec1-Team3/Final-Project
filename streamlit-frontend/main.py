# main.py

import streamlit as st
from components.login_page import login_page
from components.signup_page import signup_page

# CSS styling for the logo
st.markdown(
    """
    <style>
        .logo-container {
            display: flex;
            align-items: left;
            margin-bottom: 1em;
        }
        .logo {
            max-width: 150px;
            height: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("Job Match")

    # Logo
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="logo-container"><img class="logo" src="your_logo_url_here" alt="Logo"></div>', unsafe_allow_html=True)

    # Display Login or Signup page
    with col2:
        if 'logged_in' not in st.session_state:
            st.session_state['logged_in'] = False

        if not st.session_state['logged_in']:
            st.title("Login/Signup")
            tab1, tab2 = st.tabs(["Login", "Signup"])
            
            with tab1:
                login_page()
                
            with tab2:
                signup_page()

if __name__ == "__main__":
    main()
