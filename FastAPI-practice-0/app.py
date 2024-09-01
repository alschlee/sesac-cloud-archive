from fastapi import FastAPI
from todo import todoRouter

# FastAPI 인스턴스 생성

app = FastAPI() # api 엔드포인트 정의, http 요청 처리

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World!"}

app.include_router(todoRouter)