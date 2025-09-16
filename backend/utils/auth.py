import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from bson import ObjectId
from ..database import db, settings
from ..models.user import UserPublic

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(password: str) -> str:
	return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(password: str, password_hash: str) -> bool:
	return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))

def create_access_token(subject: str) -> str:
	now = datetime.now(timezone.utc)
	payload = {
		"sub": subject,
		"iss": settings.jwt_issuer,
		"iat": int(now.timestamp()),
		"exp": int((now + timedelta(minutes=settings.jwt_exp_minutes)).timestamp()),
	}
	return jwt.encode(payload, settings.jwt_secret, algorithm="HS256")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserPublic:
	try:
		payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"], options={"verify_aud": False})
		user_id = payload.get("sub")
		if not user_id:
			raise ValueError("No subject")
	except Exception:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

	# changed code: try converting to ObjectId when querying the users collection
	user = None
	try:
		user = await db.users.find_one({"_id": ObjectId(user_id)})
	except Exception:
		# fallback: try raw string (if you stored string ids)
		user = await db.users.find_one({"_id": user_id})

	if not user:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
	user["_id"] = str(user["_id"])  # ensure string id
	return UserPublic(**user)

def require_admin(user: UserPublic) -> None:
	if user.role != "admin":
		raise HTTPException(status_code=403, detail="Admin access required")
