from fastapi import FastAPI
import time
from . import models
from .routers import auth, posts, users, votes
from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from .config import settings

# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(posts.router)
# app.include_router(votes.router)


@app.get("/")
async def root():
    return {"message": "Pehle talish lat de!!-- totala seth \U0001f600 \U0001F606"}
