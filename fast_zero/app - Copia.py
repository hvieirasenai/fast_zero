from fastapi import FastAPI

app = FastAPI()


# @app.get('/teste')
@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
 #    return 'Teste de aplicação na WEB com chocolate!'
