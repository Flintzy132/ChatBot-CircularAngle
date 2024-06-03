import json
import os

with open('data.json', 'r') as file:
    data = json.load(file)

with open('data1.json', 'r') as file:
    data2 = json.load(file)

with open('intents.json', 'r') as file:
    intent = json.load(file)


def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)


def replace():
    data = load_json('data.json')
    data2 = load_json('data1.json')
    intent = load_json('intents.json')

    save_json('data.json', data2)
    check_nested_dict(intent)


def check_nested_dict(intent):
    og_data = load_json('data.json')

    profile_data = intent.get('ProfileData', [{}])[0]
    personal_data = profile_data.get('Personal Data', [{}])[0]

    if 'NameShown' in personal_data:
        og_data['intents'][0]['responses'] = personal_data['NameShown']
    if "GESCH" in personal_data:
        og_data['intents'][6]['responses'] = personal_data['GESCH']

    identity_data = profile_data.get('Identity Data', [])
    id_map = {
        "PAN Number": 1,
        "Cell Phone": 2,
        "Personal Email ID": 3,
        "Universal Account Number": 4,
        "Aadhaar ID": 5
    }
    for item in identity_data:
        id_description = item.get('ID_Description')
        if id_description in id_map:
            og_data['intents'][id_map[id_description]]['responses'] = item.get('IDNumber')

    education_data = profile_data.get('Education Data', [])
    edu_hist = "\n".join(
        f"{entry['SLART']} - {entry['INSTI']}" for entry in education_data
    )
    if edu_hist:
        og_data['intents'][7]['responses'] = edu_hist

    if 'Organization Data' in intent['ProfileData'][0]['Organization Data']:
        organization_data = profile_data.get('Organization Data', [{}])[0]
        org_keys = ["Position", "Reporting Manager", "Grade"]
        for i, key in enumerate(org_keys, start=8):
            if key in organization_data:
                og_data['intents'][i]['responses'] = organization_data[key]

    save_json('data.json', og_data)


def replace_appraisal():
    # Load data from JSON files
    with open('intents.json', 'r') as file:
        data2 = json.load(file)
    with open('data.json', 'r') as file:
        data1 = json.load(file)

    # Initialize and populate the list of appraisal years
    years = sorted([
        doc['InfoType'].split()[-1]
        for doc in data2['ProfileData'][0]['MyDocuments']
        if 'Appraisal' in doc['InfoType']
    ])

    # Create a dictionary for quick lookup of document paths by year
    appraisal_docs = {
        doc['InfoType'].split()[-1]: doc['FilePath']
        for doc in data2['ProfileData'][0]['MyDocuments']
        if 'Appraisal' in doc['InfoType']
    }

    # Update data1 intents with the corresponding appraisal file paths
    for intent in data1['intents']:
        if 'Appraisal' in intent['tag']:
            intent_year = intent['tag'].split()[-1]
            if intent_year in appraisal_docs:
                intent['responses'] = 'Visit : http://127.0.0.1:8000/'+appraisal_docs[intent_year]

    # Save the updated data1 back to the JSON file
    with open('data.json', 'w') as file:
        json.dump(data1, file, indent=2)


def replace_salary():
    # Load data from JSON files
    with open('intents.json', 'r') as file:
        data2 = json.load(file)
    with open('data.json', 'r') as file:
        data1 = json.load(file)

    # Initialize and populate the list of appraisal years
    years = sorted([
        doc['InfoType'].split()[-1]
        for doc in data2['ProfileData'][0]['MyDocuments']
        if 'Salary Annexure' in doc['InfoType']
    ])

    # Create a dictionary for quick lookup of document paths by year
    salary_docs = {
        doc['InfoType'].split()[-1]: doc['FilePath']
        for doc in data2['ProfileData'][0]['MyDocuments']
        if 'Salary Annexure' in doc['InfoType']
    }

    # Update data1 intents with the corresponding appraisal file paths
    for intent in data1['intents']:
        if 'Salary' in intent['tag']:
            intent_year = intent['tag'].split()[-1]
            if intent_year in salary_docs:
                intent['responses'] = 'Visit : http://127.0.0.1:8000/'+salary_docs[intent_year]
    # Save the updated data1 back to the JSON file
    with open('data.json', 'w') as file:
        json.dump(data1, file, indent=2)


replace()
replace_appraisal()
replace_salary()

os.system("train.py")

