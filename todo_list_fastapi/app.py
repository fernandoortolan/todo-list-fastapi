from fastapi import FastAPI  # Importa da biblioteca fastapi o objeto FastAPI

app = FastAPI()  # Inicia uma aplicação FastAPI


@app.get('/')
def read_root():
    return {'message': 'Olá, Mundo!'}
