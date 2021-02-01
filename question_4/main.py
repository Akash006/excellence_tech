from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from database import User, Address, Submit_data

app = FastAPI()

class userData(BaseModel):
    username: str
    password: str

class userAddress(BaseModel):
    username: str
    street: str
    pincode: int
    country: str
    state: str
    phone_no: int

@app.get("/")
def root():
    return {"Message": "Welcome to question 4"}

@app.post("/register")
def register(data: userData, address: Optional[userAddress]):
    obj1 = Submit_data()
    users_data = obj1.get_userdata()
    for row in users_data:
        if data.username == row[0]:
            return {"Message": "User already exist"}

    submit = Submit_data()
    submit.user(User(username=data.username, password=data.password))
    return {"Message": "User added successfully"}

@app.post("/login")
def login(data: userData):
    obj2 = Submit_data()
    users_val = obj2.get_userdata()
    for row in users_val:
        if data.username == row[0] and data.password == row[1]:
            return {"Message": "Login successfully"}
        elif data.username == row[0] and data.password != row[1]:
            return {"Message": "Invalid Password"}
    
    return {"Message": "No user found"}

@app.post("/address")
def update_address(address: userAddress, update: bool = False):
    obj3 = Submit_data()
    user = obj3.get_userdata()
    for row in user:
        user_exist = True if userAddress.username == row[0] else False
    
    if user_exist:
        if update:
            up = Submit_data().update_address(address)
            return {"Message": "Address updates successfully"}
        else:
            up = Submit_data().address(Address(
                username = address.username,
                street = address.street,
                pincode = address.pincode,
                country = address.country, 
                state = address.state,
                phone_no = address.phone_no,
            ))
            return {"Message": "Address added successfully"}
    else:
        return {"Message": "No user found"}