from fastapi import FastAPI
from models import User
from typing import List

app = FastAPI()

users_db = []

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/users/", response_model=User)
def create_user(user: User):
    users_db.append(user)
    return user

@app.get("/users/", response_model=List[User])
def get_users():
    return users_db
