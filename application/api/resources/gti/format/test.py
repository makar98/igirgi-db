import requests

data = {'name': 'new_name'}

put = requests.put(r'http://127.0.0.1:5000/api/customer/61', data)

print(put)