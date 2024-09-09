from fastapi import APIRouter, Depends, HTTPException, status
from models.users import User, UserSignIn, UserSignUp
from sqlmodel import select

from auth.hash_password import HashPassword
from auth.jwt_handler import create_jwt
from database.connection import getSession

userRouter = APIRouter(
    tags=["Users"] # 라우트 그룹핑하기 위한 태그
)

#users = {}

hash_password = HashPassword()

# 사용자 등록
@userRouter.post("/signup", status_code=status.HTTP_201_CREATED)
async def signNewUser(data: UserSignUp, session=Depends(getSession)) -> dict:
    statement = select(User).where(User.email == data.email)
    user = session.exec(statement).first()

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail = "동일한 사용자가 존재합니다.")

    newUser = User(
        email = data.email,
        password = hash_password.hash_password(data.password),
        username = data.username,
        events = []
    )

    session.add(newUser)
    session.commit()
    
    return {"message": "정상적으로 등록되었습니다."}

# 로그인 처리
@userRouter.post("/signin")
async def signIn(data: UserSignIn, session = Depends(getSession)) -> dict:
    statement = select(User).where(User.email == data.email)
    user = session.exec(statement).first()

    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "일치하는 사용자가 존재하지 않습니다."
        )

    #if user.password != data.password:
    if hash_password.verify_password(data.password, user.password) == False:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "패스워드가 일치하지 않습니다."
        )
    return {
        "message": "로그인에 성공했습니다.",
        "access_token": create_jwt(user.email, user.id)
        }