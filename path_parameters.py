from fastapi import FastAPI, Path
import json

app= FastAPI()
def load_data():
    with open('patient.json', 'r') as f:
        data= json.load(f)
    
    return data

@app.get('/')
def msg():
    return {'msg': 'Patient data API'}

@app.get('/view')
def view():
    data= load_data()
    return data


# Path paramaters with types
@app.get('/patient/{patient_id}')
def view_patient(patient_id: int= Path(..., description='ID of patient', example= '1')):   # see in documentation
    #load all patient data
    data= load_data()

    for patient in data:
        if patient["id"]==patient_id:
            return patient
    
    return {'error':'Patient not found'}

