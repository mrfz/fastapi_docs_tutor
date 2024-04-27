from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_read_main() -> None:
	"""
	Test the read operation of the main API endpoint.

	This function sends a GET request to the root endpoint ("/") of the main API
	and checks if the response status code is 200 (indicating a successful request)
	and if the response JSON matches the expected value: {"message": "Hello World"}.

	Parameters:
	    None

	Returns:
	    None
	"""
	response = client.get('/')
	assert response.status_code == 200
	assert response.json() == {'message': 'Hello World'}
