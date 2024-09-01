from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    item: str

class TodoItem(BaseModel):
    item: str

class TodoItems(BaseModel):
    todos: List[TodoItem]