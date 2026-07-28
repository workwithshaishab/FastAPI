from fastapi import FastAPI
from typing import Annotated
from pydantic import AfterValidator

# AfterValidator is a Pydantic validation feature that lets you run your own custom validation after the built-in 
# validation has already succeeded.

app = FastAPI()

def check_age(value: int):
    if value<18:
        raise ValueError("Must be equal or more than 18.")
    return value

def validitate_item(name: str):
    if not name.startswith("item-"):
        raise ValueError("Name must starts with 'item-'")
    return name

@app.get("/age/")
async def read_age(age: Annotated[int, AfterValidator(check_age)]):
    return {"age": age}

@app.get("/items/")
async def read_items(item: Annotated[str, AfterValidator(validitate_item)]):
    return {"item", item}