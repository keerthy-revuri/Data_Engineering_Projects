import requests
import os
import pandas as pd
import time
from datetime import datetime
import openpyxl
import psycopg2
import json

class SQL_Leetcode_repo:
    def __init__(self, configs):
        self.configs = configs
        self.github_token = self.configs.get('export_config', 'GITHUB_TOKEN')
        self.url = self.configs.get('export_config', 'GITHUB_API_URL')

    def extract(self):
        # Headers for authentication (if needed)
        # headers = {
        #     'Authorization': f'token {self.token}'
        # }
        response = requests.get(self.url)
        git_contents_json_data = response.json()
        # print(f"type of git_contents_json_data - {type(git_contents_json_data)}")
        # print(git_contents_json_data)
        return git_contents_json_data

    def transform(self,git_contents_json_data):
        folder_contents = {}
        for c in git_contents_json_data:
            if c['type'] == 'dir':
                name = c['name']
                folder_contents[c['name']] = f'{self.url}/{name}'
        list_of_dicts = []
        for key, value in folder_contents.items():
            url = value
            response = requests.get(url)
            raw_json_data = response.json()
            # print(raw_json_data)

            files_names = []
            for data in raw_json_data:
                files_names.append(data['name'])

            for fi in files_names:
                file_contents = {}
                file_contents['category'] = key
                file_contents['file_names'] = fi
                list_of_dicts.append(file_contents)
        print(list_of_dicts)
        #return list_of_dicts

        df = pd.DataFrame(list_of_dicts)
        current_timestamp = datetime.now()
        df['Timestamp'] = current_timestamp
        output_directory = 'C:/Users/Public/dataeng_project_output/Github_data_to_excel'
        sub_directory = 'output'
        output_path = os.path.join(output_directory, sub_directory)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        timestamp_str = current_timestamp.strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(output_path, f'output.csv')
        # print(output_file)
        df.to_csv(output_file, index=False)
        #print(output_contents)
    #def load(self):

    def load(self):
        try:
            sql_file_path = self.configs.get('export_config', 'sql_file_Path')

        except Exception as e:
            print("please provide sql file path under export config section")
            raise e
        conn = self.get_connection()
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

        # print(f"db details---------------------- - {db_host}, {db_port}, {db_username}, {db_password}, {db_name}")
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_username,
            password=db_password,
            host=db_host,
            port=db_port
        )
        return conn
