from typing import List
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
	name: str
	email: EmailStr
	role: str = Field(default="citizen", pattern="^(citizen|admin)$")

class UserCreate(UserBase):
	password: str

class UserLogin(BaseModel):
	email: EmailStr
	password: str

class UserPublic(UserBase):
	id: str = Field(alias="_id")
	points: int = 0
	badge: str = "Bronze"
	badges: List[str] = []

	class Config:
		populate_by_name = True

class UserDB(UserBase):
	id: str = Field(alias="_id")
	password_hash: str
	points: int = 0
	badge: str = "Bronze"
	badges: List[str] = []

	class Config:
		populate_by_name = True
