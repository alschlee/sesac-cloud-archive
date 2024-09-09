# jwt로 사용자 인증, 인증된 사용자의 user id 반환하는 함수

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from auth.jwt_handler import verify_jwt

# 요청이 들어올 때, Authorization 헤더에 토큰 추출
oauth2_schme = OAuth2PasswordBearer(tokenUrl = "/user/signin")

async def authenticate(token: str = Depends(oauth2_schme)):
    if not token:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "액세스 토큰이 누락되었습니다.")
    payload = verify_jwt(token)
    return payload["user_id"]