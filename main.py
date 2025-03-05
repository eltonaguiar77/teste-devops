from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def helloWorld():
    return {"message": "Hello World"}


@app.get("/teste1")
async def funcaoteste1():
    return {"Teste": "Deu certo!"}

@app.get("/teste2")
async def funcaoteste2():
    return {"Teste": "Deu certo de novo!"}

@app.get("/teste3")
async def funcaoteste3():
    return {"Teste": True, "num_aleatorio:" : random.randint(0, 1000)}