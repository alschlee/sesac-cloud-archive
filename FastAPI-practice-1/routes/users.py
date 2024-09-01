from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

userRouter = APIRouter(
    tags=["Users"] # 라우트 그룹핑하기 위한 태그
)

users = {}

# 사용자 등록
@userRouter.post("/signup")
async def signNewUser(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "동일한 사용자가 존재합니다."
        )
    users[data.email] = data
    return {"message": "정상적으로 등록되었습니다."}

# 로그인 처리
@userRouter.post("/signin")
async def signIn(data: UserSignIn) -> dict:
    if data.email not in users:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "일치하는 사용자가 존재하지 않습니다."
        )
    user = users[data.email]
    if user.password != data.password:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "패스워드가 일치하지 않습니다."
        )
    return {"message": "로그인에 성공했습니다."}