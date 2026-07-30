from fastapi import FastAPI, Body
# Body() is a FastAPI function that tells FastAPI: "Read this parameter from the HTTP request body."
# It also lets you add validation and metadata (title, description, examples, embed, etc.).
from pydantic import BaseModel
from  typing import Annotated

app= FastAPI()

class Item(BaseModel):
    name: str
    description: str | None= None
    price: float
    tax: float | None= None

class User(BaseModel):
    username: str
    fullname: str

@app.post("/items/")
async def create_items(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: Annotated[int, Body(title= "Importance Level", description= "Priority of the item")]):
# async def update_item(item_id: int, item: Annotated[Item, Body(embed= True)])
    results={"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


# embed=True changes how the request body JSON is structured.
# FastAPI embed the body in a key even when there is only a single parameter declared.
# It matters when there is only one body parameter.