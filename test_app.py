from fastapi.testclient import TestClient
from app import app

Client = TestClient(app)

def test_homepage():
	response = Client.get("/")
	assert response.status_code == 200
	assert "<title>M Imaad Iqbal Portfolio</title>" in response.text