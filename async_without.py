from fastapi import FastAPI
import time

app= FastAPI()
@app.get("/")
def home():
    time.sleep(5)   # paused for 5 seconds
    return {'message':'hello'}