from fastapi import FastAPI, Query, HTTPException
import json
app= FastAPI()

def load_data():
    with open('patient.json', 'r') as f:
        data= json.load(f)
        return data
    
@app.get('/sort')
def sort_patients(
    sort_by: str= Query(..., description= 'Sort on basis of age'), 
    order: str= Query('asc', description= 'Sort in ascending order')):
    valid_field= ['age']

    if sort_by not in valid_field:
        raise HTTPException(status_code= 400, detail= 'Inavalid request')
    
    data= load_data()
    reverse = order.lower() == "desc"    # order.lower()== "desc" returns true or false 
    data = sorted(data, key=lambda x: x[sort_by], reverse=reverse)    # The key tells Python what value to use for sorting.If sort_by= "age" then lambda becomes lambda x: x["age"]
    return data
