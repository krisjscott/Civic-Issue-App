from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from ..database import db
from ..models.issue import IssueCreate, IssuePublic
from ..models.user import UserPublic
from ..utils.auth import get_current_user, require_admin
from ..utils.points import add_points

router = APIRouter()

@router.post("/", response_model=IssuePublic, status_code=201)
async def create_issue(payload: IssueCreate, user: UserPublic = Depends(get_current_user)):
	now = datetime.utcnow()
	doc = {
		"title": payload.title,
		"description": payload.description,
		"category": payload.category,
		"location": payload.location.model_dump(),
		"image_url": payload.image_url,
		"status": "pending",
		"reported_by": user.id,
		"votes": 0,
		"voted_user_ids": [],
		"createdAt": now,
		"updatedAt": now,
	}
	result = await db.issues.insert_one(doc)
	doc["_id"] = str(result.inserted_id)
	await add_points(user.id, 10)
	return IssuePublic(**doc)

@router.get("/mine", response_model=List[IssuePublic])
async def my_issues(user: UserPublic = Depends(get_current_user)):
	cursor = db.issues.find({"reported_by": user.id}).sort("createdAt", -1)
	items: List[IssuePublic] = []
	async for doc in cursor:
		doc["_id"] = str(doc["_id"])  # ensure string id
		items.append(IssuePublic(**doc))
	return items

@router.get("/", response_model=List[IssuePublic])
async def list_all(status: Optional[str] = Query(None, pattern="^(pending|in-progress|resolved)$"), user: UserPublic = Depends(get_current_user)):
	require_admin(user)
	query = {}
	if status:
		query["status"] = status
	cursor = db.issues.find(query).sort([("status", 1), ("votes", -1), ("createdAt", -1)])
	items: List[IssuePublic] = []
	async for doc in cursor:
		doc["_id"] = str(doc["_id"])  # ensure string id
		items.append(IssuePublic(**doc))
	return items

@router.patch("/{issue_id}/status", response_model=IssuePublic)
async def update_status(issue_id: str, status_value: str = Query(..., pattern="^(pending|in-progress|resolved)$"), user: UserPublic = Depends(get_current_user)):
	require_admin(user)
	issue = await db.issues.find_one({"_id": ObjectId(issue_id)})
	if not issue:
		raise HTTPException(status_code=404, detail="Issue not found")

	if status_value == "resolved" and issue.get("status") != "resolved":
		await add_points(issue["reported_by"], 50)

	await db.issues.update_one({"_id": issue["_id"]}, {"$set": {"status": status_value, "updatedAt": datetime.utcnow()}})
	updated = await db.issues.find_one({"_id": issue["_id"]})
	updated["_id"] = str(updated["_id"])  # ensure string id
	return IssuePublic(**updated)

@router.post("/{issue_id}/upvote")
async def upvote_issue(issue_id: str, user: UserPublic = Depends(get_current_user)):
	issue = await db.issues.find_one({"_id": ObjectId(issue_id)})
	if not issue:
		raise HTTPException(status_code=404, detail="Issue not found")

	user_id_str = user.id
	voters = set(issue.get("voted_user_ids", []))
	if user_id_str in voters:
		return {"message": "Already upvoted"}

	voters.add(user_id_str)
	await db.issues.update_one(
		{"_id": issue["_id"]},
		{"$set": {"voted_user_ids": list(voters)}, "$inc": {"votes": 1}},
	)
	await add_points(issue["reported_by"], 1)
	return {"message": "Upvoted"}
