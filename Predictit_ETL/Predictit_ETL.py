import requests
import pandas as pd
import time
from datetime import datetime
import os
import psycopg2
import json
from pandas import json_normalize

class Predict:

    def __init__(self, configs):
        self.configs = configs
        #print(f"configs - {self.configs}")
    def extract(self):
        try:
            url = self.configs.get('export_config', 'url')

        except Exception as e:
            print(" please provide the url in configs under export config section")
            raise e

        res = requests.get(url)
        raw_json_data = res.json()
        # write data to a folder - raw files, open that file in extract function
        raw_files_directory = self.configs.get('export_config', 'raw_path_directory')
        if not os.path.exists(raw_files_directory):
             os.makedirs(raw_files_directory)

        raw_file_path = self.configs.get('export_config', 'raw_file_path')
        with open(raw_file_path, 'w') as file:
            json.dump(raw_json_data, file, indent = 4)
       # return raw_json_data

    def transform(self):
        #read json raw file in this transform function
        json_data_path  = self.configs.get('export_config', 'raw_file_path')
        with open(json_data_path , 'r') as file:
            json_data = json.load(file)

        #print(f"json_data {json_data}")
        final = []
        new_key = 'contract_id'
        old_key = 'id'
        timestr = datetime.now().isoformat()
        for data in json_data['markets']:
            market_id = data['id']
            market_url = data['url']
            for contract in data['contracts']:
                #print(f"contract - {contract}")
                contract.update({'current_time': timestr})
                contract['market_id'] = market_id
                contract['market_url'] = market_url
                del contract['dateEnd']
                # contract['new_image'] = contract['image'].str.split('/').str[-1]
                contract[new_key] = contract.pop(old_key)
                final.append(contract)
        print(final)
        df = pd.DataFrame(final)
        #print(f"df - {df}")
        #print(f"df.columns - {df.columns}")
        # splitting string using delimeter and returning last element - 3 ways to do it - use lambda or general function or use directly

        # df['new_image'] = df['image'].str.split('/').str[-1]

        # replace '.' with '_' in "az620379.vo.msecnd"  column image

        def get_last_element(image):
            final = image.split('/')
            x = final[2].replace('.', '_')
            for str in final:
                if str == final[2]:
                    final[2] = x
            output = '/'.join(final)
            return output

        df['new_image'] = df['image'].apply(get_last_element)

        #print(f"new_column - {df['new_image']}")
        #print(f"dataframe - {df.columns}")
        #print(f"dataframe - {df}")

        # timestr = datetime.now().isoformat()
        # print(timestr)
        # output_directory = 'C:/Users/Public'
        # if not os.path.exists(output_directory):
        #     os.makedirs(output_directory)
        output_file = 'C:/Users/Public/dataeng_project_output/output.csv'
        #print("hello")
        #print(output_file)
        df.to_csv(output_file, index=False)

    def load(self):
        try:
            sql_file_path = self.configs.get('export_config', 'sql_file_Path')

        except Exception as e:
            print("please provide sql file path under export config section")
            raise e
        conn =  self.get_connection()
        # Create a cursor object
        cur = conn.cursor()

        with open(sql_file_path, 'r') as file:
            sql_statements = file.read()

        # Split the contents into individual SQL statements
        sql_statements = sql_statements.split(';')

        # Remove empty statements
        sql_statements = [stmt.strip() for stmt in sql_statements if stmt.strip()]

        # Execute each SQL statement
        for stmt in sql_statements:
            print(f"stmt - {stmt}")
            cur.execute(stmt)
            conn.commit()

        # Close the cursor
        cur.close()

        # Close the connection
        conn.close()

    def get_connection(self):

        try:
            db_host = self.configs.get('database_configuration', 'host')
            db_port = self.configs.getint('database_configuration', 'port')
            db_username = self.configs.get('database_configuration', 'user')
            db_password = self.configs.get('database_configuration', 'password')
            db_name = self.configs.get('database_configuration', 'dbname')

        except Exception as e:
            print("provide db credentials in configs under database configuration section")
            raise e

        #print(f"db details---------------------- - {db_host}, {db_port}, {db_username}, {db_password}, {db_name}")
         # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_username,
            password=db_password,
            host= db_host,
            port= db_port
        )
        return conn





