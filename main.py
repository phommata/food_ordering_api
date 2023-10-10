from fastapi import FastAPI

from menu import menu_router


app = FastAPI()

app.include_router(menu_router, prefix="/menu", tags=["menu"])
