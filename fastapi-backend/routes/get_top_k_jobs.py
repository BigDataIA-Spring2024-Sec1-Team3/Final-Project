import boto3
import configparser
from sentence_transformers import SentenceTransformer
import torch
from pinecone import Pinecone
from connections import aws_connection, pinecone_connection

config = configparser.ConfigParser()
config.read('configuration.properties')

def fetch_text_data():

    try:
        s3_client, bucket_name = aws_connection()

        # Folder containing txt files
        txt_files_folder = config['s3-bucket']['text_folder_name']

        paginator = s3_client.get_paginator('list_objects_v2')
        response_iterator = paginator.paginate(
            Bucket=bucket_name,
            Prefix=txt_files_folder
        )

        # Fetching files in pdf_folder
        for response in response_iterator:
            if 'Contents' in response:
                for item in response['Contents']:
                    if str(item['Key']).endswith('.txt'):
                        key_path = item['Key']
                        response = s3_client.get_object(
                            Bucket=bucket_name, Key=key_path)
                        text = response['Body'].read().decode('utf-8')

        return text

    except Exception as e:
        print("Exception in fetch_text_data function: ", e)
        return ''


def fetch_from_pinecone():
    '''
    function to fetch data from pinecone
    '''
    try:
        # Pinecone
        pinecone_api_key, index_name = pinecone_connection()
        pinecone = Pinecone(api_key=pinecone_api_key)

        # fetching data from pinecone
        index = pinecone.Index(name=index_name)
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        if device != 'cuda':
            model = SentenceTransformer('all-MiniLM-L6-v2', device=device)

        query = fetch_text_data()
        xq = model.encode(query).tolist()
        xc = index.query(vector=xq, top_k=10, include_metadata=True)

        for match in xc['matches']:
            score = match['score']
            text = match['metadata']['text']
            print(f"{round(score, 2)}: {text}")

        # fetching data from pinecone namespace
    except Exception as e:
        print("Exception in fetch_from_pinecone() function: ", e)
        return "failed"


if __name__ == "__main__":
    fetch_from_pinecone()
