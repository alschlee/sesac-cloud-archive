from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes.users import userRouter
from routes.events import eventRouter
from database.connection import conn

@asynccontextmanager
async def lifespan(app: FastAPI):
    conn()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(userRouter, prefix = "/user")
app.include_router(eventRouter, prefix = "/event")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)