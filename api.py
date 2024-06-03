import os

import requests
import json

url = "https://weatworktest.mahyco.com/webapi/api/MyProfile/GetMyProfileData"
headers = {
    "Authorization": "bearer Q_QCrVHc-lsk_TgYuDkkSeMfEY57COGdwlxRAcDWBN0h4pfuS-6hGe5JBh0zlSKYLNqsl6gLNrzyK_F_-dl1a_wWTBGn0B5nyafx4ewWKL6noOacc3Gy_ozXnAYlpPTrvlWDpg4Ck6siVh4n9oyii9ee5MjgqM2lv7ijeCY7xB0SwNDeixsYvH_J8PAZGGux2gX5kMLZ8mlu4uBUFVzDwQ"}
data = {"loginDetails": {
    "LoginEmpID": "97260738",
    "LoginEmpCompanyCodeNo": "4000"
}
}

response = requests.post(url, headers=headers, json=data)

with open('intents.json', 'w') as file:
    json.dump(response.json(), file, indent=2)
