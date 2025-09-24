from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, Docker + FastAPI"}

@app.get("/saudacao/{nome}")
def saudar(nome: str):
    return {"mensagem": f"Olá, {nome}!"}