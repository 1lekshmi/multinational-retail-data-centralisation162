import pandas as pd
import tabula
import requests
import json
import boto3


class DataExtractor:
    """
    DateExtractor

    This class is used to extract the information from multiple sources
    """

    def read_rds_table(self,engine,table):
        """
        This function is used to read the tables in the relational database
        """
        with engine.connect() as connection:
            return pd.read_sql_table(table_name=table, con=connection)
        
    def retrieve_pdf_data(self,link):
        """
        This function is used to retrieve the data from a pdf link
        """
        pdf_link = link
        link_df = tabula.read_pdf(pdf_link,pages='all')
        link_df = pd.concat(link_df)
        return link_df
    
    def list_number_of_stores(self, endpoint, key):
        """
        This function is used to list the number of stores
        """
        response = requests.get(endpoint,headers=key)
        info = response.text
        info_json = json.loads(info)
        number_of_stores = info_json['number_stores']
        return number_of_stores
    
    def retrieve_stores_data(self,endpoint, number_of_stores, key):
        """
        This function is used to retrieve the data in the stores
        """
        stores_data = []

        for i in range(number_of_stores):
            response = requests.get(f"{endpoint}{i}", headers=key)
            info = response.text
            info_json = json.loads(info)
            stores_data.append(info_json)

        stores_df = pd.DataFrame(stores_data)
        return stores_df
    
    def extract_from_s3(self,s3_address):
        """
        This function is used to extract the data from S3 bucket
        """
        if 's3://' in s3_address:
            s3_address = s3_address.replace('s3://','')
        elif 'https://' in s3_address:
            s3_address = s3_address.replace('https://','')

        bucket_name, file_key = s3_address.split('/',1)
        bucket_name = 'data-handling-public'

        s3_client = boto3.client('s3')
        s3_data = s3_client.get_object(Bucket=bucket_name,Key=file_key)
        data = s3_data.get('Body')
        if 'csv' in file_key:
            s3_df = pd.read_csv(data)
        elif 'json' in file_key:
            s3_df = pd.read_json(data)

        return s3_df
