from jose import JWTError, jwt
from fastapi import HTTPException
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPECTED_AUDIENCE = os.getenv("EXPECTED_AUDIENCE")


def decode_access_token(token: str) -> dict:
    try:
        print(f"Decoding token: {token}")  # Debug: Print token to check the value
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], audience=EXPECTED_AUDIENCE)
        if "exp" in payload and datetime.utcfromtimestamp(payload["exp"]) < datetime.utcnow():
            raise HTTPException(
                status_code=401,
                detail="Token has expired",
            )
        return payload
    except JWTError as e:
        print(f"Error decoding token: {e}")  # Debug: Print error message
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

# Get the current user from the decoded JWT payload
def get_current_user(token: str) -> dict:
    payload = decode_access_token(token)
    return {"username": payload["sub"]}  # Assuming 'sub' is the username or user id
