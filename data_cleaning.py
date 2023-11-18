import pandas as pd
import numpy as np


class DataCleaning:
    """
    DataCleaning

    This class is used to clean the different data extracted from multiple sources
    
    """

    def clean_user_data(self,legacy_users_data):
        """
        This function is used to clean the users data table
        """
        # NULL values
        legacy_users_data.replace('NULL',np.nan,inplace=True)
        legacy_users_data.dropna(inplace=True)

        # errors on dates
        legacy_users_data['date_of_birth'] = pd.to_datetime(legacy_users_data['date_of_birth'],errors='ignore')
        legacy_users_data['join_date'] = pd.to_datetime(legacy_users_data['join_date'],errors='coerce')
        legacy_users_data = legacy_users_data.dropna(subset='join_date')

        # incorrectly typed values
        legacy_users_data = legacy_users_data.drop_duplicates(subset=['email_address'])
        need_to_replace = ['.', ' ']
        for i in need_to_replace:
            legacy_users_data['phone_number'] = legacy_users_data['phone_number'].str.replace(i,'')

        # rows filled with wrong information
        legacy_users_data.drop(legacy_users_data.columns[0],axis=1, inplace=True)

        return legacy_users_data
    
    def clean_card_data(self, card_data_table):
        """
        This function is used to clean the card data table
        """
        # NULL values
        card_data_table.replace('NULL',np.nan,inplace=True)
        card_data_table.dropna(subset=['card_number'],how='any',axis=0,inplace=True)

        # # errors with formatting
        card_data_table['card_number'] = card_data_table['card_number'].apply(str)
        card_data_table = card_data_table[~card_data_table['card_number'].str.contains('[a-zA-Z?]',na=False)]
        
        return card_data_table
    
    def clean_store_data(self, store_data_table):
        """
        This function is used to clean the store data table
        """
        store_data_table = store_data_table.reset_index(drop=True)
        #NULL values
        store_data_table.replace('NULL',np.nan,inplace=True)

        store_data_table.drop(store_data_table.columns[0], axis=1,inplace=True)
        store_data_table.drop(columns='lat',inplace=True)
        
        store_data_table['opening_date'] = pd.to_datetime(store_data_table['opening_date'],errors='coerce')
        store_data_table['staff_numbers'] = pd.to_numeric(store_data_table['staff_numbers'],errors='coerce')
        store_data_table.dropna(subset=['staff_numbers'],axis=0,inplace=True)

        store_data_table['continent'] = store_data_table['continent'].str.replace('eeEurope','Europe')
        store_data_table['continent'] = store_data_table['continent'].str.replace('eeAmerica','America')

        return store_data_table
    
    def convert_product_weights(self,weight):
        """
        This function converts the weights into kg
        """
        if 'kg' in weight:
            weight = weight.replace('kg','')
            weight = float(weight)
        elif 'g' in weight:
            weight = weight.replace('g','')
            weight = float(weight) / 1000
        elif 'ml' in weight:
            weight = weight.replace('ml','')
            weight = float(weight) / 1000
        elif 'oz' in weight:
            weight = weight.replace('oz','')
            weight = float(weight) * 0.0283495
        
        return weight
    
    def clean_products_data(self,s3_data_table):
        """
        This function cleans the products data table
        """
        s3_data_table.drop(s3_data_table.columns[0],axis=1,inplace=True)

        s3_data_table.replace('NULL',np.nan,inplace=True)
        s3_data_table.dropna(inplace=True)

        s3_data_table['date_added'] = pd.to_datetime(s3_data_table['date_added'],errors='coerce')
        s3_data_table.dropna(subset=['date_added'],inplace=True)

        s3_data_table['weight'] = s3_data_table['weight'].apply(lambda x: x.replace(' .',''))

        #temporary columns to calculate the weight of objects that give their weigh as 12 x 100g 
        temp_columns = s3_data_table.loc[s3_data_table.weight.str.contains('x'), 'weight'].str.split('x',expand=True) 
        #splits the suffix from the weight
        weights = temp_columns[1].str.split('(\d+\.?\d*)',expand=True)
        #extracts only the numbers 
        nums = temp_columns.apply(lambda x: pd.to_numeric(x.str.extract('(\d+\.?\d*)', expand=False)))
        #total weight
        new_weight = nums.prod(axis=1)
        #total weight + suffix
        final_weight = new_weight.astype(str) + weights[2]
        #replaces the weight with final weight
        s3_data_table.loc[s3_data_table.weight.str.contains('x'), 'weight'] = final_weight

        #converts the weight into kg
        s3_data_table['weight'] = s3_data_table['weight'].apply(lambda x: self.convert_product_weights(x))

        return s3_data_table
    
    def clean_orders_data(self,orders_table):
        """
        This function cleans the orders table
        """

        orders_table.drop(columns='first_name',axis=1,inplace=True)
        orders_table.drop(columns='last_name',axis=1,inplace=True)
        orders_table.drop(columns='1',axis=1,inplace=True)
        orders_table.drop(columns='level_0',axis=1,inplace=True)
        orders_table.drop(orders_table.columns[0],axis=1,inplace=True)

        return orders_table
    
    def clean_date_table(self,date_table):
        """
        This function cleans the date table
        """
        date_table['year'] = pd.to_datetime(date_table['year'],errors='coerce').dt.year.convert_dtypes()
        date_table['month'] = pd.to_datetime(date_table['month'],errors='coerce',format='%m').dt.month.convert_dtypes()
        date_table['day'] = pd.to_datetime(date_table['day'],errors='coerce',format='%d').dt.day.convert_dtypes()
        date_table['timestamp'] = pd.to_datetime(date_table['timestamp'],errors='coerce',format='%H:%M:%S').dt.time
        date_table.dropna(inplace=True)

        return date_table  
