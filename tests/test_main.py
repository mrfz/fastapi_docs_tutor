from fastapi.testclient import TestClient
import pytest


from src.main import app, Item

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


@pytest.mark.parametrize(
	(
		'name',
		'description',
		'price',
		'tax',
		'expected_status_code',
		'expected_response',
	),
	(
		('Foo', None, 32.99, None, 200, {'name': 'Foo', 'price': 32.99}),
		('Foo', None, 32.99, 4.99, 200, {'name': 'Foo', 'price': 32.99, 'tax': 4.99}),
		(
			'Foo',
			'A product',
			32.99,
			4.99,
			200,
			{'name': 'Foo', 'description': 'A product', 'price': 32.99, 'tax': 4.99},
		),
		(
			'Foo',
			'A product',
			32.99,
			None,
			200,
			{'name': 'Foo', 'description': 'A product', 'price': 32.99},
		),
		(
			None,
			None,
			32.99,
			4.99,
			422,
			{
				'detail': [
					{
						'loc': ['body', 'name'],
						'msg': 'field required',
						'type': 'value_error.missing',
					}
				]
			},
		),
		(
			'Foo',
			'A product',
			None,
			4.99,
			422,
			{
				'detail': [
					{
						'loc': ['body', 'price'],
						'msg': 'field required',
						'type': 'value_error.missing',
					}
				]
			},
		),
	),
)
def test_post_item(
	name: str,
	description: str,
	price: float,
	tax: float,
	expected_status_code: int,
	expected_response: dict[str, str],
) -> None:
	"""
	Test the create operation of the main API endpoint.

	This function sends a POST request to the "items/" endpoint of the main API
	and checks if the response status code is as expected and if the response JSON
	matches the expected value.

	Parameters:
		name (str): The name of the item.
		description (str): The description of the item.
		price (float): The price of the item.
		tax (float): The tax of the item.
		expected_status_code (int): The expected status code of the response.
		expected_response (dict): The expected response JSON.

	Returns:
		None
	"""

	response = client.post(
		'/items/',
		json={'name': name, 'description': description, 'price': price, 'tax': tax},
	)

	assert response.status_code == expected_status_code
	# assert response.json() == expected_response
