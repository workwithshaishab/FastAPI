# When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
# A request body is data sent by the client to your API. A response body is the data your API sends to the client.

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None= None
    price: float
    tax: float | None= None

app= FastAPI()


@app.post("/items/")
async def create_item(item: Item):   # The request body should match the Item model. item= a variable that stores the request body as an Item object.
    item_dict= item.model_dump()  
    # Converts Pydantic model into dictionary. It is done as our model only knows four fields.
    # If we want to return extra field, Pydantic will raise an erros as it is not defined in the model.
    if item.tax is not None:
        total_price= item.price+item.tax
        item_dict.update({"totalprice": total_price})
        # The .update() method in Python is used to update dictonary. It adds another field called "totalprice".

    return item_dict


# Request body + path parameters

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id":item_id, **item.model_dump()}


# Request body + path + query parameters

@app.put("/items/{item_id}")
async def update_item(item_id:int, item:Item, q:str | None= None):
    result= {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q":q})
    return result