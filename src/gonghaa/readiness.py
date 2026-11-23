from typing import Literal

from pydantic import BaseModel


class Readiness(BaseModel):
    status: Literal["ready"] = "ready"
