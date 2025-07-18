import pytest
from app import app
import json


@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get('/ping')
    assert response.status_code == 200

def test_invalid_dob_format(client):
    """DOB in wrong format should trigger exception"""
    data = {
        "name": "Broken",
        "dob": "15-06-2000"  # wrong format
    }
    response = client.post("/", data=data)
    assert b"Error in processing DOB" in response.data

def test_dob_before_1800(client):
    """DOB before 1800 should trigger error"""
    data = {
        "name": "Oldie",
        "dob": "1700-01-01"
    }
    response = client.post("/", data=data)
    assert b"DOB year must be after 1800" in response.data



