"""Docstrings"""
import json
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

r = requests.post("http://127.0.0.1:8000/", data=json.dumps(data))

print(r.json())
