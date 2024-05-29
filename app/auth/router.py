from fastapi import APIRouter


router = APIRouter()


#login
@router.post("/signin")
def sign_in():
    pass


#signup
@router.post("/signup")
def sign_up():
    pass