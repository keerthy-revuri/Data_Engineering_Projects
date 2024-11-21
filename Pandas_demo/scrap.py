import json
import pandas as pd
from pandas import json_normalize

# Sample JSON data as a string
json_data = '''
{
    "markets ": [
        {
            "id": 6865,
            "name": "Which party will win the 2024 U.S. presidential election?",
            "shortName": "Which party wins the presidency in 2024?",
            "contracts": 
                [{
                    "id": 23547,
                    "dateEnd": "NA"
                },
                {
                    "id": 23548,
                    "dateEnd": "NA"
                }
                ],
            "address": [
                "a", "b"
            ]

        },
         {
            "id": 7013,
            "name": "Will a woman be elected U.S. president in 2024?",
            "shortName": "Woman president elected in 2024?",
            "contracts": [
                {
                    "id": 24594,
                    "dateEnd": "NA"
                },
                {
                    "id": 24595",
                    "dateEnd": "NA"   
                }
                ],
         "address": [
                "c", "d"
            ]
         }
    ]        
} 
'''

# Load the JSON data
data = json.loads(json_data)

# Flatten the JSON data
# Normalize the 'contracts' data and keep metadata fields from the 'markets' list
df = json_normalize(
    data['markets'],
    record_path='contracts',
    meta=['id', 'name', 'shortName'],
    sep='_'
)

# Initialize an empty list to store the expanded 'address' data
expanded_addresses = []

# Expand the 'address' data to match the number of rows in the DataFrame
for market in data['markets']:
    # Calculate the number of contracts in this market
    num_contracts = len(market['contracts'])
    # Repeat the address list for the number of contracts
    expanded_addresses.extend(market['address'] * num_contracts)

# Add the expanded 'address' data to the DataFrame
df['address'] = expanded_addresses

print(df)

# final = []
#         new_key = 'contract_id'
#         old_key = 'id'
#         timestr = datetime.now().isoformat()
#         for data in json_data['markets']:
#             market_id = data['id']
#             market_url = data['url']
#             for contract in data['contracts']:
#                 print(f"contract - {contract}")
#                 contract.update({'current_time': timestr})
#                 contract['market_id'] = market_id
#                 contract['market_url'] = market_url
#                 del contract['dateEnd']
#                 # contract['new_image'] = contract['image'].str.split('/').str[-1]
#                 contract[new_key] = contract.pop(old_key)
#                 final.append(contract)
#         print(final)
# df = pd.DataFrame(final)