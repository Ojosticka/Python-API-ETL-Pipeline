import requests
import pandas as pd
from cred import headers

url = "https://covid-193.p.rapidapi.com/countries"

response = requests.get(url, headers=headers)

print(response.json())