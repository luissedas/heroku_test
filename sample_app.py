"""Docstrings"""
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class TaggedItem(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name: str
    tags: Union[str, list]
    item_id: int

app = FastAPI()

@app.post("/items/")
async def create_item(item: TaggedItem):
    """docstring"""
    return item

@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    """docstring"""
    return {"fetch": f"Fetched {count} of {item_id}"}
