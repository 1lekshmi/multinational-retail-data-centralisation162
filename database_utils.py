import yaml
import psycopg2
from sqlalchemy import create_engine, inspect


class DatabaseConnector:
    """
    DatabaseConnector(yaml_file: str)

    This class is used to connect to both local database and relational AWS database

    Attributes:
        yaml_file(str): a yaml file name containing the information needed to connect to the databases
    """

    def __init__(self, yaml_file):
        self.yaml_file = yaml_file
        
    def read_db_creds(self):
        """
        This function is used to read the credentials saved in the yaml_file
        """
        with open(self.yaml_file, 'r') as file:
            creds = yaml.safe_load(file)
        return creds
    
    def init_db_engine(self,creds):
        """
        This function is used to initialise the engine using the credentials from the yaml_file
        """
        engine = create_engine(f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")
        return engine
    
    def list_db_tables(self,engine):
        """
        This function is used to list all the tables in the database
        """
        engine.connect()
        inspector =inspect(engine)
        return inspector.get_table_names()
    
    def upload_to_db(self, data_frame, table_name, creds):
        """
        This function is used to upload the cleaned data into the local database
        """
        local_engine = create_engine(f"{creds['LOCAL_DATABASE_TYPE']}+{creds['LOCAL_DB_API']}://{creds['LOCAL_USER']}:{creds['LOCAL_PASSWORD']}@{creds['LOCAL_HOST']}:{creds['LOCAL_PORT']}/{creds['LOCAL_DATABASE']}")
        local_engine.connect()
        data_frame.to_sql(table_name, local_engine, if_exists='replace')
