from tkinter import Message
from .models.model import User
from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
async def hello():
    message = "hey bitches mes"
    return message

@app.post("/createUser")
async def createUser(user:User):
    return{"message":"Created User","data":user}


@app.post("/createuserwithAdd")
async def createUserwithAdd(user:User):
    return user