from fastapi import FastAPI
from routes import blog_get


app = FastAPI()
app.include_router(blog_get.router)

@app.get('/')
def get():
    return {"message": "Hola mundo"}
