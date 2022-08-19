from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing  import Optional
from random import randrange


app = FastAPI()

class Post(BaseModel):
  title: str
  content: str
  published: bool = True
  rating: Optional[int] = None


my_posts = [{
  "id": 1,
  "title": "post 1",
  "content": "The content of post 1"
},
{
  "id": 2,
  "title": "post 2",
  "content": "The content of post 2"
}]

def find_post(id):
  for p in my_posts:
    print(p["id"])
    if p['id'] == int(id):
      return p

@app.get("/")
def root():
  return {"message": "Hello world!! to me"}


@app.get("/posts/{id}")
def get_post_by_id(id: int, response: Response):
  post = find_post(id)
  if not post:
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
  return {"data": post}


@app.get("/posts")
def get_posts():
  return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
  post_dict = post.dict()
  post_dict['id'] = randrange(0, 1000000 )
  my_posts.append(post.dict())
  return {"data": my_posts}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
  post = find_post(id)
  if not post:
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
  my_posts.pop(post['id'])
  return {'message': 'post was deleted successfully'}