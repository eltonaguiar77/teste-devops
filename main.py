import random
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def helloWorld():
    return {"message": "Hello World"}


@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num aleatorio": random.randint(0, 20000)}
