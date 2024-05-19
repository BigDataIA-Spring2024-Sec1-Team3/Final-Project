# JobMatch - Job Recommendation System 

## Live application links

[![codelab](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1xOJo6D40dsWjctPaj2Z7uZlOG9cHrW0DRejiGDkK9XM#0)

[![Demo](https://img.shields.io/badge/Demo_Link-808080?style=for-the-badge&logo=YouTube&logoColor=white)](https://youtu.be/yw4AyXYgTtY)

## Technologies Used
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Amazon AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Snowflake](https://img.shields.io/badge/Snowflake-0093F1?style=for-the-badge&logo=snowflake&logoColor=white)](https://www.snowflake.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FF9900?style=for-the-badge)](https://huggingface.co/docs/transformers/en/model_doc/bert)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Airflow](https://img.shields.io/badge/Airflow-FF4B4B?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)](https://airflow.apache.org/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)](https://www.selenium.dev/)
[![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Pinecone](https://img.shields.io/badge/Pinecone-220052?style=for-the-badge)](https://www.pinecone.io/)

## Overview

JobMatch is a revolutionary Job Recommendation System designed to streamline and enhance the job search experience by centralizing the job search process and by analyzing user uploaded resumes. JobMatch provides tailored job recommendations from top platforms like LinkedIn, Indeed, and SimplyHired. Users gain direct access to recommended job listings, ensuring a personalized and efficient job search experience.

## Problem Statement

### Challenge:
The current scenario for the job search process is really tiresome and exhilarating for job seekers. A user currently has to go through every job portal manually, browse through the available jobs, and make a profile describing the role he/she is targeting; which consumes a lot of time. We wanted to optimize the process by making an application that will bring jobs from different portals and filter them based on the user's resume, by using modern technologies, hence easing the process for job seekers.

### Solution:
The objective of this project is to develop and deploy an efficient data engineering infrastructure for a Job Recommendation System, termed "JobMatch," which facilitates the seamless matching of job seekers with relevant employment opportunities based on their uploaded resumes. Unlike traditional job search platforms, JobMatch will aggregate jobs from several portals, utilize advanced data processing techniques to analyze the content of user's resumes, and recommend suitable job openings from various sources such as LinkedIn, Indeed, and SimplyHired. The system will not only match job seekers with relevant positions but also provide direct access to the recommended job listings through provided links.

## Architecture:

![Alt text](./architecture-diagram/flow_diagram.png)

## Codelab
Link: https://codelabs-preview.appspot.com/?file_id=1xOJo6D40dsWjctPaj2Z7uZlOG9cHrW0DRejiGDkK9XM#0

## Project Tree

```
📦 
├─ .gitignore
├─ README.md
├─ airflow
│  ├─ .gitignore
│  ├─ Dockerfile
│  ├─ configuration.properties.example
│  ├─ dags
│  │  ├─ embed
│  │  │  ├─ configuration.properties.example
│  │  │  ├─ connections.py
│  │  │  └─ embed_and_upsert.py
│  │  ├─ extract
│  │  │  ├─ configuration.properties.example
│  │  │  ├─ connections.py
│  │  │  ├─ extract_indeed_jobs.py
│  │  │  ├─ extract_linkedin_jobs.py
│  │  │  └─ extract_simplyhired_jobs.py
│  │  ├─ load
│  │  │  ├─ configuration.properties.example
│  │  │  ├─ connections.py
│  │  │  └─ loading.py
│  │  ├─ pipeline_indeed.py
│  │  ├─ pipeline_linkedin.py
│  │  ├─ pipeline_simplyhired.py
│  │  └─ validate
│  │     ├─ configuration.properties.example
│  │     ├─ connections.py
│  │     └─ validation.py
│  ├─ docker-compose.yaml
│  └─ requirements.txt
├─ architecture-diagram
│  ├─ flow_diagram.ipynb
│  ├─ flow_diagram.png
│  └─ input_icons
│     ├─ huggingface.png
│     ├─ indeed.png
│     ├─ linkedin.png
│     ├─ openai.png
│     ├─ pdf.png
│     ├─ pinecone.png
│     ├─ streamlit.png
│     ├─ user-authentication.png
│     └─ user.png
├─ cloudbuild.yaml
├─ docker-compose.yaml
├─ fastapi-backend
│  ├─ Dockerfile
│  ├─ configuration.properties.example
│  ├─ connections.py
│  ├─ main.py
│  ├─ requirements.txt
│  ├─ routes
│  │  ├─ analyticsRoute.py
│  │  ├─ authRoute.py
│  │  └─ userRoutes.py
│  └─ test_api.py
├─ requirements.txt
├─ setup
│  └─ snowflake_objects.sql
└─ streamlit-frontend
   ├─ Dockerfile
   ├─ components
   │  ├─ analytics.py
   │  ├─ get_job_matches.py
   │  ├─ login_page.py
   │  ├─ signup_page.py
   │  └─ upload_page.py
   ├─ configuration.properties.example
   ├─ main.py
   └─ requirements.txt
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)

## Prerequisites
Before running this project, ensure you have the following prerequisites set up:

- **Python**: Ensure Python is installed on your system.
- **Docker**: Ensure Docker-desktop is installed on your system.
- **Virtual Environment**: Set up a virtual environment to manage dependencies and isolate your project's environment from other Python projects. You can create a virtual environment using `virtualenv` or `venv`.
- **requirements.txt**: Install the required Python dependencies by running the command:
  ```
  pip install -r requirements.txt
  ```
- **Config File**: Set up the `configurations.properties` file with the necessary credentials and configurations.

- **Snowflake**: Use `setup/snowflake_objects.sql` to define the queries on snowflake. Also, ensure you have the necessary credentials and configurations set up in the `configurations.properties` file for connecting to Snowflake.
- **Google Cloud Platform**: Create a Google Cloud Engine. Ensure you have the necessary credentials and configurations set up in the `configurations.properties` file.

## How to Run the Application Locally

To run the application locally, follow these steps:

1. Clone the repository to get all the source code on your machine.

2. Use `source/venv/bin/activate` to activate the environment.

3. Create a configuration.properties file in the all the directories where configuration.properties.example is present. Sample config file:

```
[auth-api]
SECRET_KEY = 
ALGORITHM = 

[MongoDB]
mongo_url = 
db_name = 
collection_name = 
collection_name_markdown = 

[airflow]
base_url_airflow = 
password = 
username = 

[AWS]
access_key = 
secret_key = 
region_name = 

[s3-bucket]
bucket = 
resumes_folder_name = 
text_folder_name = 

[SNOWFLAKE]
user = 
password = 
account = 
warehouse = 
database = 
schema = 
role = 
jobsTable = 

[OPENAI]
api_key = 

[PINECONE]
pinecone_api_key = 
index = 
```

4. Once you have set up your environment variables, Use `docker-compose up - build` to run the application

5. Access the Airflow UI by navigating to http://localhost:8080/ in your web browser.

6. Once the DAGs have run successfully, view the Streamlit application

7. Access the Streamlit UI by navigating to http://localhost:8501/ in your web browser.

8. Enter username and password if you've already logged in. Otherwise you can register yourself and then run the application.


## Team Contribution

WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

| Name                      | Contribution % |
| ------------------------- | -------------- |
| Muskan Deepak Raisinghani | 33.3%          |
| Rachana Keshav            | 33.3%          |
| Ritesh Choudhary          | 33.3%          |
