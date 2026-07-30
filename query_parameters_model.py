# If you have a group of query parameters that are related, you can create a Pydantic model to declare them.

# This would allow you to re-use the model in multiple places and also to declare validations and metadata for all the parameters at once. 


from typing import Annotated, Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

# Literal is used to restrict a value to one or more fixed choices.
# Field is used inside a Pydantic model to add validation and metadata to model fields.

app= FastAPI()

class ProductFilter(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length= 40, description="Product Name")]
    price: Annotated[float, Field(gt=0, description="Product Price")]
    category: Literal["Laptop", "Phone", "Airpods"]

@app.get("/products/")
# Without Query(), FastAPI would assume the model comes from the request body. 
async def get_products(product: Annotated[ProductFilter, Query()]):   # Instead of reading JSON from the request body, FastAPI reads from the URL.
    return product