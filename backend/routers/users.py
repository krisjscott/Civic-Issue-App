from fastapi import APIRouter, Depends
from ..models.user import UserPublic
from ..utils.auth import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserPublic)
async def get_me(user: UserPublic = Depends(get_current_user)):
	return user
