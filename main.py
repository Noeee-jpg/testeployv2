from fastapi import FastAPI
from config import engine

import tables.users as users_table

import routes.users as users_routes

users_table.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_routes.router)

@app.get("/")
async def roof ():
    return "hello world"