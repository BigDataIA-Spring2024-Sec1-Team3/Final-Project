from streamlit_modal import Modal
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

    resume_names = getResumeList()

    selected_resume = st.selectbox("Select a resume", resume_names)

    if selected_resume:
        st.write(f"You selected resume: {selected_resume}")

        st.button("Get Job Matches")
        view_button = st.button("View Resume")

        modal = Modal(
            key="resume_modal",
            title="Resume",
            padding=50,
            max_width=1000
        )

        if view_button:
            modal.open()

        if modal.is_open():
            with modal.container():
                access_token = st.session_state['access_token']
                headers = {"Authorization": f"Bearer {access_token}"}
                base_url = config['APIs']['base_url_auth']
                url = base_url + f"userRoutes/getResume/?file_name=" + selected_resume
                response = requests.get(
                    url, headers=headers)
                if response.status_code == 200:
                    st.markdown(
                        f'<iframe src="{url}" width="1000" height="1000"></iframe>', unsafe_allow_html=True)
                else:
                    st.error("Failed to fetch the resume.")
