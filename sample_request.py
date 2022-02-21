"""Docstrings"""
import json
import requests

DATA = {"name":"Hitchhiking Kit", "tags":["book", "towel"],
        "item_id":23}

REQ = requests.post("http://127.0.0.1:8000/items/", data=json.dumps(DATA))

print(REQ.json())
