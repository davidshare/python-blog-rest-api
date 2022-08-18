from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
  return {"message": "Hello world!! to me"}


@app.get("/posts")
def get_posts():
  return {"data": "posts"}

@app.post("/createpost")
def create_post(payload: dict = Body(...)):
  print(payload)
  return {"new_post": f"title {payload['title']} content {payload['content']}"}