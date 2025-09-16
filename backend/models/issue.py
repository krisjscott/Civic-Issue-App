from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

ISSUE_CATEGORIES = ("pothole", "garbage", "water", "streetlight", "other")

class Location(BaseModel):
	lat: float
	lng: float
	address: str

class IssueCreate(BaseModel):
	title: str
	description: str
	category: str = Field(pattern="^(pothole|garbage|water|streetlight|other)$")
	location: Location
	image_url: Optional[str] = None

class IssuePublic(BaseModel):
	id: str = Field(alias="_id")
	title: str
	description: str
	category: str
	location: Location
	image_url: Optional[str] = None
	status: str
	reported_by: str
	votes: int
	createdAt: datetime
	updatedAt: datetime

	class Config:
		populate_by_name = True
