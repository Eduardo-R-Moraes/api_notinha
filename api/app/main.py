from fastapi import FastAPI
from nota.NotaController import router as NotaRouter

app = FastAPI()

app.include_router(NotaRouter)

@app.get('/')
def ola_mundo():
    return 'ola mundo'