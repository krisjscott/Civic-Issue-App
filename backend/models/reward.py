from pydantic import BaseModel

class RedeemRequest(BaseModel):
	points: int = 100

class RedeemResponse(BaseModel):
	voucher_code: str
	remaining_points: int
