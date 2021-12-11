from enum import Enum
from typing import Optional
from fastapi import FastAPI, status
from starlette.responses import Response


app = FastAPI()


@app.get('/')
def get():
    return {"message": "Hola mundo"}


@app.get('/all')
def get_all(page=1, page_size: Optional[int] = None):
    return {"message": f'All {page} on page {page_size}'}


@app.get('/{id}')
def get_by_id(id: int):
    return {"userId": id}


class DocType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/object/{type}')
def getDocType(type: DocType):
    return {"message": f'Doc with type {type}'}


@app.get('/object/value/{id}', status_code=status.HTTP_200_OK)
def get_object(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'object {id} not found'}
    elif id <= 5 and id >= 0:
        response.status_code = status.HTTP_200_OK
        return {'message': f'object {id}'}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'error': 'bad request'}
