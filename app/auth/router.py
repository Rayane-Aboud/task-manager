from fastapi import APIRouter


router = APIRouter()


#login
@router.post("/signin")
async def sign_in():
    return {}


#signup
@router.post("/signup")
async def sign_up():
    return {}