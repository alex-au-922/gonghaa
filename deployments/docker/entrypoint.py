import os

from asyncpg import connect
from fastapi import FastAPI

from gonghaa.readiness import Readiness

app = FastAPI(title="GongHaa")


@app.get("/readyz")
async def ready() -> Readiness:
    database = await connect(os.environ["DATABASE_URL"], timeout=5, command_timeout=5)
    try:
        await database.execute("SELECT 1")
    finally:
        await database.close(timeout=5)
    return Readiness()
