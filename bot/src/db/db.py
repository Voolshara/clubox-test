from os import getenv
import asyncio

from dotenv import load_dotenv
from tortoise import Tortoise

load_dotenv("../.env")

CONNECTION_STRING = "postgres://{}:{}@{}:{}/{}".format(
    getenv("PG_USER"),
    getenv("PG_PASSWORD"),
    getenv("PG_HOST"),
    getenv("PG_PORT"),
    getenv("PG_DBNAME"),
)

async def init_db():
    await Tortoise.init(
        db_url=CONNECTION_STRING,
        modules={'models': ['src.db.models']}
    )
    await Tortoise.generate_schemas()

def run_init_db():
    asyncio.run(init_db())