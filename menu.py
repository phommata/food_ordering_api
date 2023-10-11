import json
from fastapi import APIRouter
from models.menu import Menu
from typing import List

menu_router = APIRouter()

class MenuItem:
    def __init__(self, id, name, genre, price):
        self.id = id
        self.name = name
        self.genre = genre
        self.price = price

class MenuService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MenuService, cls).__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        self.menu_items = [
            MenuItem("781d66c4-87aa-469f-88df-1117c77fb576", "Brooklyn Spaghetti", "ITALIAN", 14.99),
            MenuItem("b9024fb1-c3d9-4c5f-b447-0826e86988b4", "Lamb Gyro", "GREEK", 12.99),
            MenuItem("f4f81a55-8f3d-4ae1-ae80-c81f51c0c49c", "Cheeseburger", "AMERICAN", 9.99),
        ]

    def get_menu_items(self) -> List[MenuItem]:
        return self.menu_items

# Initialize the MenuService
menu_service = MenuService()

@menu_router.get("/", response_model=Menu)
async def get_menu():
    menu_items = menu_service.get_menu_items()
    menu_items_dicts = [menu.__dict__ for menu in menu_items]
    
    return {"items": menu_items_dicts}
