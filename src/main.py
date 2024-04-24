from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{'item_name': 'Foo'}, {'item_name': 'Bar'}, {'item_name': 'Baz'}]


@app.get('/')
async def root() -> dict[str, str]:
	return {'message': 'Hello World'}


@app.get('/items/')
async def read_items(skip: int = 0, limit: int = 10) -> list[dict[str, str]]:
	"""Get all items

	Args:

		skip (int, optional): skip first n items. Defaults to 0.

		limit (int, optional): maximum number of items. Defaults to 10.
	Returns:

		list[dict[str, str]]: list of items
	"""

	return fake_items_db[skip : skip + limit]


@app.get('/items/{item_id}')
async def read_item(
	item_id: str, q: str | None = None, short: bool = False
) -> dict[str, str]:
	"""Get an item

	Args:

		item_id (str): item id

		q (str | None, optional): query. Defaults to None.

	Returns:

		dict[str, str]: item
	"""
	item = {'item_id': item_id}
	if q:
		item.update({'q': q})
	if not short:
		item.update(
			{'description': 'This is an amazing item that has a long description'}
		)
	return item


@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(
	user_id: int, item_id: str, q: str | None = None, short: bool = False
) -> dict[str, object]:
	"""Get an user item

	Args:

		user_id (int): user id

		item_id (str): item id

		q (str | None, optional): query. Defaults to None.

		short (bool, optional): short. Defaults to False.

	Returns:

		dict[str, object]: item
	"""
	item = {'item_id': item_id, 'owner_id': user_id}
	if q:
		item.update({'q': q})
	if not short:
		item.update(
			{'description': 'This is an amazing item that has a long description'}
		)
	return item


@app.get('/items/{item_id}')
async def read_item_required(
	item_id: str, needy: str, skip: int = 0, limit: int | None = None
) -> dict[str, object]:
	"""Get an item

	Args:

		item_id (str): item id

		needy (str): needy

		skip (int, optional): skip first n items. Defaults to 0.

		limit (int | None, optional): maximum number of items. Defaults to None.
	Returns:

		dict[str, object]: item
	"""
	item = {'item_id': item_id, 'needy': needy, 'skip': skip, 'limit': limit}
	return item
