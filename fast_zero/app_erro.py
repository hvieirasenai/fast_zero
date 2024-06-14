from fastapi import FastAPI

app = FastAPI()


# @app.get('/teste')
@app.get('/')
def read_root():
    return {'message': 'Olár Mundis! ... Cacildis'}


#    return {"message": "Olár Mundis! ... Cacildis"}
#    return 'Teste de aplicação na WEB com chocolate!'
# este arquivo para testar o ruff
