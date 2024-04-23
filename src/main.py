from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def root(item_id: int) -> dict[str, int]:
    """Response to a GET request

    Args:
        item_id (int): item_id number to return

    Returns:
        dict[str, int]: dict response
    """
    return {"item_id": item_id}

# Order matters!
@app.get("/users/me")
async def read_user_me() -> dict[str, str]:
    """Response to a GET request
    
    Returns:
        dict[str, str]: dict response
    """
    return {"username": "current_user"}


@app.get("/users/{username}")
async def read_user(username: str) -> dict[str, str]:
    """Response to a GET request
    
    Args:
        username (str): username to return

    Returns:
        dict[str, str]: dict response
    """
    return {"username": username}