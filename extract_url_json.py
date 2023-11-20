'''This script is used to extract url's from json given the file provided by user should be .json format'''

import json

file_name = input("Please provide filename in .json format:")
with open(file_name,'r') as file:
    data =  json.load(file)
final_data = data['results']
for url in data:
    print(url['url'])
