from fastapi import FastAPI
import asyncio

app = FastAPI()

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")
    return "Result 1"

async def task2():
    print("Task 2 started")
    await asyncio.sleep(3)
    print("Task 2 finished")
    return "Result 2"

@app.get("/")
async def home():
    result1, result2=  await asyncio.gather(task1(), task2())
    return{
        'task1': result1,
        'task2': result2
    }