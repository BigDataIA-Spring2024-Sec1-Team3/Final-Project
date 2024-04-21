#Import dependencies
import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import time
from datetime import date
import concurrent.futures
import os
from connnections import aws_connection, snowflake_connection

def scrape_jobs(job_titles, location):
    try:
        jobs_df = pd.DataFrame(columns=["job_id","job_title","company","location","job_url", "date_posted","job_desc"])
        
        # construct URL for LinkedIn job search
        for title in job_titles:
            start= -10 # starting point for pagination
            count_of_jobs_scraped = 0
            while count_of_jobs_scraped < 15:
                time.sleep(3) 
                start += 10
                li_url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?f_TPR=r86400&keywords={title}&location={location}&start={start}"
                # print(count_of_jobs_scraped,li_url)
                try:
                    
                    # Send a GET request to the URL and store the response
                    response = requests.get(li_url)
                                        
                    if response.status_code == 200:    
                        # Find all list items(jobs postings)
                        list_data = response.text
                        list_soup = BeautifulSoup(list_data, "html.parser")
                        page_jobs = list_soup.find_all("li")
                        
                        if page_jobs:
                            
                            #Itetrate through job postings to find job ids
                            for job in page_jobs:
                                base_card_div = job.find("div", {"class": "base-card"})
                                job_id = base_card_div.get("data-entity-urn").split(":")[3]
                                
                                time.sleep(3)
                                job_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
                                
                                # Send a GET request to the job URL and parse the reponse
                                job_response = requests.get(job_url)
                                job_soup = BeautifulSoup(job_response.text, "html.parser")
                                
                                # Try to extract and store the job title
                                if count_of_jobs_scraped < 15:
                                    if job_response.status_code == 200:
                                        # extract job title
                                        try:
                                            j_title = job_soup.find("h2", {"class":"top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title"}).text.strip().replace("|"," ")
                                        except:
                                            j_title = None
                                            
                                        # extract company name
                                        try:
                                            company_name = job_soup.find("a", {"class": "topcard__org-name-link topcard__flavor--black-link"}).text.strip().replace("|"," ")
                                        except:
                                            company_name = None
                                            
                                        # extract job description
                                        try:
                                            job_desc_div = job_soup.find("div", {"class":"show-more-less-html__markup"})
                                            job_desc = job_desc_div.get_text().strip().replace("|"," ")
                                        except:
                                            job_desc=None
                                        
                                        # extract job location
                                        try:
                                            job_location = job_soup.find("span", {"class":"topcard__flavor topcard__flavor--bullet"}).text.strip().replace("|"," ")
                                        except:
                                            job_location = None
                                        
                                        # appending row to dataframe
                                        jobs_df.loc[len(jobs_df)] = [job_id, j_title, company_name, job_location, f"https://www.linkedin.com/jobs/view/{job_id}", str(date.today()), job_desc]
                                        count_of_jobs_scraped+=1   
                                else:
                                    break
                        else:
                            print("No more jobs available")
                            break
                                    
                except Exception as e:
                    print("Exception in scrape_jobs func: ",e)
        
        return jobs_df
        
    except Exception as e:
        print("Exception: ",e)
        
        return jobs_df
    
def load_into_snowflake():
    try:
        # Loading csv to S3
        client, bucket = aws_connection()
        response = client.upload_file("./linkedin_temp.csv", bucket, "jobs/linkedin_job.csv")

        # Loading from s3 to snowflake table
        conn, job_table = snowflake_connection()
        cur = conn.cursor() # Create a cursor
        load_query=f'''COPY INTO {job_table} 
                FROM @jobs_stage/linkedin_jobs.csv 
                FILE_FORMAT = (FORMAT_NAME = 'PIPE_SEPARATED_FF') ON_ERROR=CONTINUE;'''

        # Execute query to fetch rows from the Snowflake table
        cur.execute(load_query)
        
        # Delete the temporary csv file
        os.remove("./linkedin_temp.csv")
        
        return "Success"
    
    except Exception as e:
        print("Exception in load_into_snowflake function: ", e)   
        return "Failed"
            

job_titles = ['Data Engineer','Software Engineer','Data Analyst','Data Scientist','Backend Developer','UI UX Developer','Financial Analyst','Product Manager','Supply Chain Manager','Front End Developer']
location = "United States"
df = scrape_jobs(job_titles, location)

df.to_csv("linkedin_temp.csv", index=False, sep="|")

res = load_into_snowflake()
print(res)