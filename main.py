from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/teste1")
async def funcaoteste():
    return {"Teste": "Deu certo!"}

@app.get("/teste2")
async def funcaoteste1():
    return {"Teste": "Deu certo de novo!"}