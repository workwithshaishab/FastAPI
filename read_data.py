from fastapi import FastAPI
import json

app= FastAPI()

def load_data():
    with open('patient.json', 'r')as f:
        data= json.load(f)

    return data

@app.get("/")
def msg():
    return {'message': 'Patient System API'}

@app.get("/about")
def msg():
    return {'message': 'API to manage patient records'}
    

@app.get("/view")
def view():
    data= load_data()
    return data