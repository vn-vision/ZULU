import requests

# the api endpoint, gets information from the views

endpoint = 'http://localhost:8000/api/'

res = requests.get(endpoint)
print(res.text)
print(res.status_code)
print(res.json()['Greeting'])