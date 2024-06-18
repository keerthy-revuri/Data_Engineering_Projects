import pandas as pd

persons = [{'name' : "keerthy",
           'email' : 'a@gmail.com',
            'gender': 'F'
           },
            {'name' : "kujij",
           'email' : 'a@gmail.com',
            'gender': 'F'
           }
           ]
df = pd.DataFrame(persons)
print(df)
print(df['email'])
print(df.email) # column can be accessed in 2 ways - [] or .
print(type(df['email'])) # this column is a series data type

print(df[['name','email']])

print(df.columns)

print("iloc")

print(df.iloc[0]) # using iloc first column will be actual column_name unlike previous actions which have first index as integers starting from 0

print(f"iloc - {df.iloc[[0,1], 2]}") # prints 2 rows of data - only emails with indexes as left column

print("loc")

print(df.loc[0])

print(df.loc[[0,1], ['email', 'name']]) # in loc column name can be given as 2nd argument unlike i iloc

#loc - label based indexing
#iloc - integer based indexing


