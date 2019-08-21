# coding: utf-8
"""A hello-world API; small, but perfectly formed.
"""

from fastapi import FastAPI, Query
from pydantic import BaseModel


api = FastAPI("hello-world")  # pylint: disable=invalid-name


class Greeting(BaseModel):  # pylint: disable=too-few-public-methods
    """Response issued by the / endpoint.
    """

    greeting: str


@api.get("/", response_model=Greeting)
def hello_world(name: str = Query("world")):
    """Returns a friendly greeting.
    """
    return {"greeting": f"Hello, {name}!"}
