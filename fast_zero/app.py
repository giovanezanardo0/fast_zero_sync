from fastapi import FastAPI
from http import HTTPStatus
from fast_zero.schemas import Message, UserSchema, UserPublic, UserDB

app = FastAPI()

database = []

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    
    user_with_id = UserDB(
        id = len(database) +1,
        **user.model_dump() #transforma os dados do schema UserSchema em um dicionario
    )
    database.append(user_with_id)
    return user_with_id
