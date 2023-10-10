from pydantic import BaseModel
from typing import List

class MenuItem(BaseModel):
    id: str
    name: str
    genre: str
    price: float

class Menu(BaseModel):
    items: List[MenuItem]