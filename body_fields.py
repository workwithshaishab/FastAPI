from typing import Annotated
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

# We can declare validation and metadata inside of Pydantic models using Pydantic's Field.

app= FastAPI()

class Item(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=40, description= "Product Name")]
    price: Annotated[int, Field(gt=0, description= "Price of the Product")]

@app.put("/items/{item_id}")
async def update_item(item_id:int, item: Annotated[Item, Body(embed= True)]):
    results={"item_id": item_id, "item": item}
    return results


# # embed=True changes how the request body JSON is structured.
# FastAPI embed the body in a key even when there is only a single parameter declared.
# It matters when there is only one body parameter.