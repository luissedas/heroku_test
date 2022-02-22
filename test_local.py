"""DOCSTRINGS"""
from fastapi.testclient import TestClient
from main import app

def test_get_path():
    client = TestClient(app)
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Welcome to Earth!"}


def test_post_class1():
    client = TestClient(app)
    r = client.post("/", json={
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
    })
    assert r.status_code == 200, "Failed"
    assert r.json() == {"prediction": ">50K"}


def test_post_class2():
    client = TestClient(app)
    r = client.post("/", json={
        "age": 18,
        "workclass": "Private",
        "education": "HS-grad",
        "marital-status": "Never-married",
        "occupation": "Own-child",
        "relationship": "Husband",
        "race": "Black",
        "sex": "Male",
        "hours-per-week": 10,
        "native-country": "United-States"
    })
    assert r.status_code == 200
    assert r.json() == {"prediction": "<=50K"}
