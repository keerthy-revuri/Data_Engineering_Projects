import requests
import pandas as pd
import time
from datetime import datetime
import os

res = requests.get("https://www.predictit.org/api/marketdata/all/")
print(res.json())
json_data = res.json()
final = []
new_key = 'contract_id'
old_key = 'id'
timestr = datetime.now().isoformat()
for data in json_data['markets']:
    market_id = data['id']
    market_url = data['url']
    for contract in data['contracts']:
        print(contract)
        contract.update({'current_time':timestr})
        contract['market_id'] = market_id
        contract['market_url'] = market_url
        del contract['dateEnd']
        #contract['new_image'] = contract['image'].str.split('/').str[-1]
        contract[new_key] = contract.pop(old_key)
        final.append(contract)

print(final)
df = pd.DataFrame(final)

#splitting string using delimeter and returning last element - 3 ways to do it - use lambda or general function or use directly

#df['new_image'] = df['image'].str.split('/').str[-1]

#replace '.' with '_' in "az620379.vo.msecnd"  column image

def get_last_element(image):
    final = image.split('/')
    x = final[2].replace('.', '_')
    for str in final:
        if str == final[2]:
            final[2] = x
    output = '/'.join(final)
    return output

df['new_image'] = df['image'].apply(get_last_element)


print(f"new_column - {df['new_image']}")
print(f"dataframe - {df.columns}")
print(f"dataframe - {df}")

# timestr = datetime.now().isoformat()
# print(timestr)
output_directory = 'C:/Users/Public/dataeng_project_output'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
output_file = os.path.join(output_directory, 'output.csv')
print(output_file)
df.to_csv(output_file, index = False)






