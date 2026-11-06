from tokenize import String

from pydantic import BaseModel



class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    email:str
    address:Address