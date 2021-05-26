from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root(name: str, age: Optional[int] = None):
    return {'Hello': name, 'Age': age}
