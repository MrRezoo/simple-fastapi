from typing import Optional

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    username: str
    email: EmailStr


@app.post('/user/', response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserIn):
    if user.username.lower() == 'admin':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='username cant be `admin`',
                            headers={
                                'name': 'reza'
                            })
    return user
