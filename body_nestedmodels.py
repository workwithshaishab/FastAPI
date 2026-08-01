from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    age: int
    hobbies: list[str]
    address: Address   # Nested Model

class Company(BaseModel):
    company_name: str
    employee: list[User]

@app.post("/users/")
async def create_user(user: User):
    return user

@app.post("/companies/")
async def create_company(company: Company):
    return company