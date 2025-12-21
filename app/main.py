from fastapi import FastAPI

from . import consumer_router, producer_router


app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(consumer_router)
app.include_router(producer_router)
