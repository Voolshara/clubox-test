from contextlib import asynccontextmanager
from datetime import datetime
from typing import Dict, Any

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from src.common import time_until_birthday
from src.db.db import init_db, register_tortoise, CONNECTION_STRING
from src.models.user_model import BirthData, User_model, User_birth_response
from src import crud

from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # do sth before db inited
    async with register_tortoise(
        app,
        db_url=CONNECTION_STRING,
        modules={"models": ["src.db.schemas"]},
        add_exception_handlers=True,
    ):
        # do sth while db connected
        yield
    # do sth after db closed

app = FastAPI(title="WebbApp server", lifespan=lifespan)
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", summary="Check responsibility")
def root():
    return {"message": "It's working"}

@app.get("/user/{tg_id}", response_model=User_birth_response, summary="Get user data")
async def user(tg_id: int):
    db_user = await crud.get_user_data(tg_id)
    if db_user:
        days, hours, minutes = time_until_birthday(db_user.date_birth)
        return User_birth_response(
            **db_user.__dict__,
            birth_data=BirthData(
                days_for_birth = days,
                minutes_for_birth = minutes,
                hours_for_birth = hours
                ),
            )
    raise HTTPException(status_code=404, detail="Bad request")

@app.post("/user/", response_model=User_birth_response, summary="Add user")
async def create_user(user: str):
    print(user)
    db_user = await crud.add_user(user=user)
    days, hours, minutes = time_until_birthday(db_user.date_birth)
    return User_birth_response(
        **db_user.__dict__,
        birth_data=BirthData(
            days_for_birth = days,
            minutes_for_birth = minutes,
            hours_for_birth = hours
        ),
        )
