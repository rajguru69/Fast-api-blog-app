from typing import Optional
from fastapi import FastAPI, HTTPException, Response
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from starlette import status

app = FastAPI()

try:
    conn = psycopg2.connect(host="localhost", database="", user="postgres", password="")
    cur = conn.cursor()
except Exception as e:
    print(f'Error connecting to database: {e}')


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_post = [{"title": "My first post", "content": "This is my first post", "id": 1},
           {"title": "My second post", "content": "This is my second post", "id": 2}]


def find_post_by_id(post_id):
    for post in my_post:
        if post["id"] == post_id:
            return post


def find_index_of_post(post_id):
    for index, post in enumerate(my_post):
        print(index, post, post_id, my_post)
        if post["id"] == post_id:
            return index, post
    return None, None


@app.get("/")
async def root():
    return {"message": "Hello Sir/Ma'am"}


@app.get("/posts")
def get_posts():
    return {"data": my_post}


@app.post("/createpost")
def create_post(new_post: Post):
    post_dict = new_post.dict()
    post_dict["id"] = randrange(0, 100000)
    my_post.append(post_dict)
    return {"data": my_post}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post_by_id(id)
    if not post:
        raise HTTPException(status_code=404, detail={"data": "Not found", "status": status.HTTP_404_NOT_FOUND})
    return {"data": f"here is my post {post}"}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # breakpoint()
    post_index, post = find_index_of_post(id)
    if not post_index:
        raise HTTPException(status_code=404, detail={"data": f"post with id {id} not found"})
    my_post.pop(post_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, updated_post: Post):
    print(updated_post.dict())
    post_index, post = find_index_of_post(id)
    if not post_index:
        raise HTTPException(status_code=404, detail={"data": f"post with id {id} not found"})
    updated_post_dict = updated_post.dict()
    updated_post_dict["id"] = id
    my_post[post_index] = updated_post_dict
    return {"data": updated_post.dict(), "message": "post updated successfully."}