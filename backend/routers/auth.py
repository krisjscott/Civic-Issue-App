from fastapi import APIRouter, HTTPException, status, Depends
from bson import ObjectId
from ..database import db
from ..models.user import UserCreate, UserLogin, UserPublic
from ..utils.auth import hash_password, verify_password, create_access_token, get_current_user

router = APIRouter()

@router.post("/signup", response_model=UserPublic, status_code=201)
async def signup(payload: UserCreate):
	existing = await db.users.find_one({"email": payload.email})
	if existing:
		raise HTTPException(status_code=409, detail="Email already registered")

	doc = {
		"name": payload.name,
		"email": payload.email,
		"password_hash": hash_password(payload.password),
		"role": payload.role or "citizen",
		"points": 0,
		"badge": "Bronze",
		"badges": ["Bronze"],
	}
	result = await db.users.insert_one(doc)
	doc["_id"] = str(result.inserted_id)
	return UserPublic(**doc)

@router.post("/login")
async def login(payload: UserLogin):
	user = await db.users.find_one({"email": payload.email})
	if not user or not verify_password(payload.password, user["password_hash"]):
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

	token = create_access_token(str(user["_id"]))
	return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserPublic)
async def me(current_user: UserPublic = Depends(get_current_user)):
	return current_user
