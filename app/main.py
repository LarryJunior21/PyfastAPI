from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from .auth import get_current_user

app = FastAPI()

# OAuth2PasswordBearer is used here for documentation purposes.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "Hello from Supabase-auth FastAPIya!"}

# Protected endpoint that expects the token in the Authorization header
@app.get("/protected-endpoint")
def protected_endpoint(token: str = Depends(oauth2_scheme)):
    # Use the `get_current_user` function to validate and decode the token
    user = get_current_user(token)
    return {"message": "Access granted", "user": user}
