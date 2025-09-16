import random
from fastapi import APIRouter, Depends, HTTPException
from ..models.reward import RedeemRequest, RedeemResponse
from ..models.user import UserPublic
from ..utils.auth import get_current_user
from ..utils.points import add_points
from ..database import db

router = APIRouter()

VOUCHERS = ["AMAZON100", "FLIPKART200", "SWIGGY50", "ZOMATO75", "PAYTM100"]

@router.post("/redeem", response_model=RedeemResponse)
async def redeem(payload: RedeemRequest, user: UserPublic = Depends(get_current_user)):
	current = await db.users.find_one({"_id": user.id}, {"points": 1})
	if not current or current.get("points", 0) < payload.points:
		raise HTTPException(status_code=400, detail="Not enough points to redeem")

	remaining, _ = await add_points(user.id, -abs(payload.points))
	code = random.choice(VOUCHERS)
	return RedeemResponse(voucher_code=code, remaining_points=remaining)
