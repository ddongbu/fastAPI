from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

import db.models as models
from db.database import engine
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic 사용 함 으로써 데이터 유효성 검사와 파싱을 처리한다.
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float

# Path: / 관리자
@app.get("/")
async def read_root():
    return {"message": "Hello Root World"}




