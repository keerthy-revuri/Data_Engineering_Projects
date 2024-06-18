import requests
payload = {'key1':'value1', 'key2':'value2'}
res = requests.post("https://httpbin.org/post", data = payload)

#print(res.text)
print(res.text)