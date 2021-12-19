from fastapi import APIRouter, status, Response
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class BlogModel(BaseModel):
    pass


@router.post('/new')
def create_blog(blog: BlogModel):
    return "ok"
