from os import getenv
import asyncio

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from contextlib import AbstractAsyncContextManager

from types import ModuleType
from typing import Dict, Iterable, Optional, Union

from tortoise import Tortoise, connections
from tortoise.exceptions import DoesNotExist, IntegrityError
from tortoise.log import logger

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

def register_tortoise(
    app: FastAPI,
    config: Optional[dict] = None,
    config_file: Optional[str] = None,
    db_url: Optional[str] = None,
    modules: Optional[Dict[str, Iterable[Union[str, ModuleType]]]] = None,
    generate_schemas: bool = False,
    add_exception_handlers: bool = False,
) -> AbstractAsyncContextManager:
    async def init_orm() -> None:  # pylint: disable=W0612
        await Tortoise.init(config=config, config_file=config_file, db_url=db_url, modules=modules)
        logger.info("Tortoise-ORM started, %s, %s", connections._get_storage(), Tortoise.apps)
        if generate_schemas:
            logger.info("Tortoise-ORM generating schema")
            await Tortoise.generate_schemas()

    async def close_orm() -> None:  # pylint: disable=W0612
        await connections.close_all()
        logger.info("Tortoise-ORM shutdown")

    class Manager(AbstractAsyncContextManager):
        async def __aenter__(self) -> "Manager":
            await init_orm()
            return self

        async def __aexit__(self, *args, **kwargs) -> None:
            await close_orm()

    if add_exception_handlers:

        @app.exception_handler(DoesNotExist)
        async def doesnotexist_exception_handler(request: Request, exc: DoesNotExist):
            return JSONResponse(status_code=404, content={"detail": str(exc)})

        @app.exception_handler(IntegrityError)
        async def integrityerror_exception_handler(request: Request, exc: IntegrityError):
            return JSONResponse(
                status_code=422,
                content={"detail": [{"loc": [], "msg": str(exc), "type": "IntegrityError"}]},
            )

    return Manager()

async def init_db():
    await Tortoise.init(
        db_url=CONNECTION_STRING,
        modules={'models': ['src.db.schemas']}
    )
    await Tortoise.generate_schemas()

def run_init_db():
    asyncio.run(init_db())