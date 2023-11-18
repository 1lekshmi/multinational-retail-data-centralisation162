from database_utils import DatabaseConnector
from data_cleaning import DataCleaning
from data_extraction import DataExtractor


def main():
    upload_dim_users()
    upload_dim_card_details()
    upload_dim_store_details()
    upload_dim_products()
    upload_orders_table()
    upload_dim_date_times()

def upload_dim_users():
    """
    This function is used to upload the extracted and cleaned data from a relational AWS database to local database
    
    """
    connector = DatabaseConnector('db_creds.yaml')
    extractor = DataExtractor()
    cleaner = DataCleaning()

    db_creds = connector.read_db_creds()
    engine = connector.init_db_engine(db_creds)
    tables = connector.list_db_tables(engine)
    user_table = extractor.read_rds_table(engine, tables[1])
    clean_user_table = cleaner.clean_user_data(user_table)
    clean_user_table.to_csv('users.csv')
    connector.upload_to_db(clean_user_table, 'dim_users', db_creds)

def upload_dim_card_details():
    """
    This function is used to upload the extracted and cleaned data from a pdf to local database

    """
    connector = DatabaseConnector('db_creds.yaml')
    extractor = DataExtractor()
    cleaner = DataCleaning()

    db_creds = connector.read_db_creds()
    card_data_table = extractor.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
    clean_card_data_table = cleaner.clean_card_data(card_data_table)
    clean_card_data_table.to_csv('clean_card_details.csv')
    connector.upload_to_db(clean_card_data_table, 'dim_card_details', db_creds)

def upload_dim_store_details():
    """
    This function is used to upload the extracted and cleaned data using an API to local database
    
    """
    connector = DatabaseConnector('db_creds.yaml')
    extractor = DataExtractor()
    cleaner = DataCleaning()

    number_store_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
    retrieve_store_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/'
    api_key = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
    
    db_creds = connector.read_db_creds()
    number_stores = extractor.list_number_of_stores(number_store_endpoint,api_key)
    stores_df = extractor.retrieve_stores_data(retrieve_store_endpoint,number_stores,api_key)
    clean_stores_df = cleaner.clean_store_data(stores_df)
    clean_stores_df.to_csv("clean_store_table.csv")
    connector.upload_to_db(clean_stores_df,'dim_store_details',db_creds)


def upload_dim_products():
    """
    This function is used to upload the extracted and cleaned data from an S3 bucket to local database

    """
    connector = DatabaseConnector('db_creds.yaml')
    extractor = DataExtractor()
    cleaner = DataCleaning()

    db_creds = connector.read_db_creds()
    address = 's3://data-handling-public/products.csv'

    s3_data = extractor.extract_from_s3(address)
    clean_s3_data = cleaner.clean_products_data(s3_data)
    clean_s3_data.to_csv('s3_clean_data.csv')
    connector.upload_to_db(clean_s3_data,'dim_products',db_creds)


def upload_orders_table():
    """
    This function is used to upload extracted and cleaned data from a relational AWS database to local database
    
    """
    connector = DatabaseConnector('db_creds.yaml')
    extractor = DataExtractor()
    cleaner = DataCleaning()

    db_creds = connector.read_db_creds()
    engine = connector.init_db_engine(db_creds)
    table = connector.list_db_tables(engine)
    orders_table = extractor.read_rds_table(engine,table[2])
    clean_orders_table = cleaner.clean_orders_data(orders_table)
    clean_orders_table.to_csv('clean_orders_table.csv')
    connector.upload_to_db(clean_orders_table,'orders_table',db_creds)

def upload_dim_date_times():
    """
    This function is used to upload the extracted and cleaned data from an S3 bucket to local database
    
    """
    connector = DatabaseConnector('db_creds.yaml')
    extractor = DataExtractor()
    cleaner = DataCleaning()

    db_creds = connector.read_db_creds()
    address = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'

    date_table = extractor.extract_from_s3(address)
    clean_date_table = cleaner.clean_date_table(date_table)
    clean_date_table.to_csv('clean_date.csv')
    connector.upload_to_db(clean_date_table,'dim_date_times',db_creds)
    
if __name__ == "__main__":
    main()
