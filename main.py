from fastapi import FastAPI,Request,Response
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
    return 