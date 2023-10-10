from fastapi import FastAPI

from menu import menu_router
from order import order_router

app = FastAPI()

app.include_router(menu_router, prefix="/menu", tags=["menu"])
app.include_router(order_router, prefix="/order", tags=["order"])

