from typing import Optional

from fastapi import FastAPI, Query
import pydantic

app = FastAPI()


class Person(pydantic.BaseModel):
    name: str
    age: int
    height: Optional[int] = 0


@app.post('/create')
def create_person(person: Person):
    return person

#
# @app.get('/')
# def create_person(name: Optional[str] = Query(None, max_length=10, min_length=4)):
#     return {'Hello': 'world', 'name': name}


@app.get('/')
def create_person(name: Optional[str] = Query(..., max_length=10, min_length=4)):
    return {'Hello': 'world', 'name': name}
