import re
import configparser
from PyPDF2 import PdfReader
import os
from connections import aws_connection

config = configparser.ConfigParser()
config.read('configuration.properties')


def pdf_txt_extraction():
    '''
    Function to:
        - Extract content from resume PDF files stored in AWS S3
        - Store the extracted text files back to S3
    '''
    try:
        s3_client, bucket_name = aws_connection()

        # Folder containing PDF files
        resume_files_folder = config['s3-bucket']['resumes_folder_name']

        # Folder to store extracted text files
        txt_file_folder = config['s3-bucket']['text_folder_name']

        paginator = s3_client.get_paginator('list_objects_v2')
        response_iterator = paginator.paginate(
            Bucket=bucket_name,
            Prefix=resume_files_folder
        )

        # Fetching files in pdf_folder
        for response in response_iterator:
            if 'Contents' in response:
                for item in response['Contents']:
                    if str(item['Key']).endswith('.pdf'):

                        # Download the PDF file from S3
                        input_file_path = str(item['Key']).split('/')[-1]
                        s3_client.download_file(
                            bucket_name, item['Key'], input_file_path)

                        # Extract text from the downloaded PDF file
                        text = ''
                        with open(input_file_path, 'rb') as file:
                            reader = PdfReader(file)
                            for page in reader.pages:
                                extracted_text = page.extract_text() or ''
                                # Remove extra spaces and clean up text
                                cleaned_text = re.sub(
                                    r'\s+', ' ', extracted_text).strip()
                                text += cleaned_text + ' '

                        # Join non-empty sections
                        text = ' '.join(filter(None, text.split(' ')))

                        # Delete the temporary downloaded file (pdf)
                        os.remove(input_file_path)

                        # Writing file to s3 bucket
                        file_name_wo_extension = input_file_path.rstrip('.pdf')
                        output_file_path = file_name_wo_extension + '.txt'
                        with open(output_file_path, 'w', encoding="utf-8") as file:
                            file.write(text)

                        # Upload the file to S3
                        output_file_key = txt_file_folder + output_file_path
                        response = s3_client.upload_file(
                            output_file_path, bucket_name, output_file_key)

                        # Delete the temporary downloaded file (txt)
                        os.remove(output_file_path)

        return response

    except Exception as e:
        print("Exception in pdf_txt_extraction function: ", e)
        return None


if __name__ == "__main__":
    pdf_txt_extraction()
