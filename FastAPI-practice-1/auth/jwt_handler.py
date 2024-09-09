from time import time
from fastapi import HTTPException, status
from jose import jwt
from database.connection import Settings

settings = Settings()

# JWT 생성
def create_jwt(email: str, user_id: int) -> str:
    payload = {"user": email, "user_id": user_id, "iat": time(), "exp": time() + 3600}
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256") # HS256 = HMAC + SHA256
    return token

# JWT 검증
def verify_jwt(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        exp = payload.get("exp")
        if exp is None:
            raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Invalid token")
        if time() > exp:
            raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "Token expired")
        return payload
    except:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Invalid token")