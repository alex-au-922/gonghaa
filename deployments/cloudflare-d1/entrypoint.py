from collections.abc import Awaitable
from typing import Protocol, cast

from fastapi import FastAPI, Request
from workers import asgi

from gonghaa.readiness import Readiness

app = FastAPI(title="GongHaa")


class D1Statement(Protocol):
    def first(self, column: str, /) -> Awaitable[object]: ...


class D1Database(Protocol):
    def prepare(self, sql: str, /) -> D1Statement: ...


class Bindings(Protocol):
    D1: D1Database


@app.get("/readyz")
async def ready(request: Request) -> Readiness:
    bindings = cast(Bindings, request.scope["env"])
    await bindings.D1.prepare("SELECT 1 AS ready").first("ready")
    return Readiness()


Default = asgi.entrypoint(app)
