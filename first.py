# FastAPI: FastAPI is a modern Python web framework used to build APIs (Application Programming Interfaces) quickly, efficiently, and with less code.

from fastapi import FastAPI

app= FastAPI()      # creating a FastAPI object. FastAPI() calls the constructor of the class. app represents your entire web application

@app.get("/")       # A decorator tells FastAPI: "Whenever someone sends a GET request to /, run the function below."
def hello():
    return {'message': 'Hello World'}

@app.get("/about")
def about():
    return {'message': 'I am learning FastAPI'}

@app.get("/contact")
def contact():
    return {
        'email':'hehehaha@gmail.com',
        'phone':'9841098000'
    }

@app.get("/sum")           # http://127.0.0.1:8000/sum?a=10&b=20
def sum(a: int, b: int):   # a and b are query parameters taken from the URL. : int tells FastAPI to convert and validate them as integers.
    return{
        'result':a+b
    }