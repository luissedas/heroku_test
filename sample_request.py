"""Docstrings"""
import requests

data = {
    "age": 38,
    "workclass": "Private",
    "education": "Doctorate",
    "marital-status": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "hours-per-week": 60,
    "native-country": "United-States"
}

r = requests.post("https://luis-heroku-app.herokuapp.com/",
                  json=data)

print(r.status_code)
print(r.json())
