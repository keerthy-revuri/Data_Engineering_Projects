import os
import pandas as pd

df = pd.read_csv('data/survey_results_public.csv') # reading csv file to create a dataframe
print(df)
print(df.shape) # gives total number of rows, columns
print(df.info)  # gives total number of rows, columns along with column names and data types
pd.set_option('display.max_columns', 85) # displays all 85 columns
print(df.columns)
print(df.head(10)) #displays first 10 rows
print(df.tail(10)) #displays last 10 rows

temp = []
for column in df.columns:
    temp.append(column)
print(len(temp))
columns_to_select = ['ResponseId', 'Q120']
df_output = df[columns_to_select] # new dataframe with selected columns
print(df_output)
df_output.to_csv('output.csv', index = False) # writing data frame to output csv file, first parameter is path, if index is false then index column will not be there

#df_output.to_csv('Data_Engineering_Projects/Pandas_demo/data/output.csv', index = False)

#Write output file to data folder

current_file_path = os.path.abspath(__file__) #import os library , using which current file path can be found
print(current_file_path)
current_directory = os.path.dirname(current_file_path) #gives current directory path
print(current_directory)
output_directory_path = current_directory + '\data' #adding data folder to the current directory path, we can also write output csv file here itself
print(output_directory_path)

print(os.path.join(output_directory_path, 'output.csv'))
df_output.to_csv(os.path.join(output_directory_path, 'output.csv'), index = False)

print(df['Q120'].value_counts())

print(df.loc[0:2, 'ResponseId':'Q120']) # gives data of rows - 0,1,2 with columns - ResponseId, Q120



