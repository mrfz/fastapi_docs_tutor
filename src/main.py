from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    """Class for enum test

    Args:
        str (str): string name
        Enum (Enum): enumerated value

    Returns:
        class: ModelName class
    """

    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


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


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName) -> dict[str, str]:
    """Response to a GET model request

    Args:
        model_name (ModelName): model name to return

    Returns:
        dict[str, str]: dict response
    """
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
