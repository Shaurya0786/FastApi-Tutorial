from fastapi import FastAPI,Request,Response,Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class CreatePost(BaseModel):
    title:str
    description:str
    published:bool=True
    rating:Optional[int]=None

@app.get('/')
async def root():
    return {"data":"Api is Live"}


#Post creation in db 
@app.post('/posts')
async def create_post(new_post:CreatePost): #The new_post that is being recieved should be of type CreatePost and we can use dot operator on the new_post
    print(new_post.model_dump())
    return

@app.get('/greet/{name}')
async def greetings(name:str,age:Optional[str]=None):
    return {
        "name":name,
        "age": age
    }


# Now to to access headers in python we can use the Header class and the access the headers
@app.get('/headers',status_code=500)
async def get_headers(accept:str=Header(None)):
    return {f"accept":{accept}}