import json
import os
import requests

with open('data.json', 'r') as file:
    data = json.load(file)

response = requests.get('http://127.0.0.1:8080/get-user')
hrpolicy = requests.get('http://127.0.0.1:8000/download_pdf')
api_data = response.json()


def replace_data(og_data, r_data):
    og_data['intents'][0]['responses'] = r_data[0]['Name']
    og_data['intents'][1]['responses'] = r_data[1]['Pan Card']
    og_data['intents'][2]['responses'] = r_data[2]['Birthday']
    og_data['intents'][5]['responses'] = r_data[3]['Leave Balance'][0]['Earned Leave']
    og_data['intents'][6]['responses'] = r_data[3]['Leave Balance'][1]['Casual Leave']
    og_data['intents'][7]['responses'] = r_data[5]['Supervisor'][0]['Name']
    og_data['intents'][8]['responses'] = r_data[5]['Supervisor'][1]['Contact']
    og_data['intents'][9]['responses'] = r_data[4]['HR Policy'][0]['Holiday']
    og_data['intents'][10]['responses'] = r_data[4]['HR Policy'][1]['Leaves']


replace_data(data, api_data)
print("Done")
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

os.system("train.py")
