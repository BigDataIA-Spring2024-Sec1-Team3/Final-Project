import streamlit as st
import configparser
import requests

config = configparser.ConfigParser()
config.read('./configuration.properties')

def getResumeList():
    access_token = st.session_state['access_token']

    # Define the headers with the Authorization header containing the access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    base_url = config['APIs']['base_url_auth']
    resumeList_url = base_url + "userRoutes/files"
    
    response = requests.get(resumeList_url, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        return result  # Return the list of resume names obtained from the backend
    else:
        return []  # Return an empty list if the request fails

def show_find_jobs():
    st.title("Find Jobs")
    
    resume_names=getResumeList()
    
    selected_resume = st.selectbox("Select a resume", resume_names)
    
    if selected_resume:
        st.write(f"You selected resume: {selected_resume}")
    
        st.button("Get Job Matches")
        st.button("View Resume")
        