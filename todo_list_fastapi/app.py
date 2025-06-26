from http import HTTPStatus

from fastapi import FastAPI  # Importa da biblioteca fastapi o objeto FastAPI
from fastapi.responses import HTMLResponse

from todo_list_fastapi.schemas import Message

app = FastAPI()  # Inicia uma aplicação FastAPI


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


@app.get(
    '/ola_mundo_html', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
def read_ola_mundo_html():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
      </head>
      <body>
        <h1>Olá, Mundo!</h1>
      </body>
    </html>"""
