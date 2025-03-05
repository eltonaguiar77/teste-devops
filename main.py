from fastapi import FastAPI

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