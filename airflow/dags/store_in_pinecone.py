from connections import snowflake_connection, pinecone_connection
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
import torch
import pandas as pd


def fetch_table_from_snowflake():
    '''
    function to fetch jobs data from snowflake
    '''
    try:
        conn, table = snowflake_connection()
        fetch_query = f"SELECT * FROM {table};"

        # Create a cursor
        cur = conn.cursor()

        # Execute query to fetch rows from the Snowflake table
        cur.execute(fetch_query)

        # Fetch all rows and combine summaries
        data = cur.fetchall()

        df = pd.DataFrame(data, columns=['job_id',
                                         'job_title',
                                         'company',
                                         'location',
                                         'url',
                                         'date_posted',
                                         'description'])

        return df

    except Exception as e:
        print("Exception in fetch_data_from_snowflake function", e)
        return ''


def storing_pinecone():
    '''
    function to store set a in pinecone
    '''
    try:
        df = fetch_table_from_snowflake()

        # Pinecone
        pinecone_api_key, index_name = pinecone_connection()
        pinecone = Pinecone(api_key=pinecone_api_key)
        index = pinecone.Index(name=index_name)

        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        if device != 'cuda':
            model = SentenceTransformer('all-MiniLM-L6-v2', device=device)

        all_embeddings = []

        # iterating over pandas dataframe
        print("Generating embeddings..")
        for _, row in df.iterrows():
            _id = str(row['job_id'])
            job_title = row['job_title']
            company = row['company']
            location = row['location']
            url = row['url']
            date_posted = row['date_posted']
            description = row['description']

            # Concatenating all relevant text data for embedding with new lines
            full_text = f"{job_title}\n{company}\n{location}\n{url}\n{date_posted}\n{description}"
            display_text = f"job_title: {job_title}\ncompany: {company}\nlocation: {location}\nurl: {url}\ndate_posted: {date_posted}"

            # embedding data
            embedding = model.encode(full_text)

            print(f"Embedded question for {_id}")

            embedding_data = {
                "id": _id,
                "values": embedding,
                "metadata": {
                    "id": _id,
                    "file_name": 'jobmatch_data.csv',
                    "text": display_text
                }
            }

            # embedding question and answer separately
            all_embeddings.append(embedding_data)

        print("Embeddings generated")

        # upserting the embeddings to pinecone namespace
        index.upsert(all_embeddings)

        return "successful"

    except Exception as e:
        print("Exception in storing_pinecone() function: ", e)
        return "failed"


if __name__ == "__main__":
    # function to store data into pinecone
    result = storing_pinecone()
