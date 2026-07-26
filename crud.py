from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI()

# Pydantic Model
class Product(BaseModel):
    name: str
    price: float
    description: str
    quantity: int

# For temporary data
products= {}

@app.get("/")
def home():
    return {"message": "Welcome to CRUD API"}

# CREATE
@app.post("/products/{product_id}")
def create_product(product_id: int, product:Product):
    if product_id in products:
        raise HTTPException(
            status_code= 400,
            detail= "Product ID already exists."
        )

    products[product_id]= product  # FastAPI converts the JSON into a Product object
    # products[1] = Product( name="Laptop",description="Dell Inspiron", price=85000,quantity=5)


# READ
@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products:
        raise HTTPException(
            status_code= 404,
            detail= "Product not found"
        )
    return products[product_id]


# UPDATE
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    if product_id not in products:
        raise HTTPException(
            status_code= 404,
            detail= "Product not found"
        )
    products[product_id]= product

    return {"message": "Product updated successfully", "updated_product":product}


# DELETE
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in products:
        raise HTTPException(
            status_code= 404,
            detail= "Product not found"
        )

    deleted_product= products.pop(product_id)
    return {"message": "Product deleted successfully", "deleted_product": deleted_product}