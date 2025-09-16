from typing import Tuple
from bson import ObjectId
from ..database import db


def compute_badge(points: int) -> str:
    if points >= 1000:
        return "Platinum"
    if points >= 500:
        return "Gold"
    if points >= 100:
        return "Silver"
    return "Bronze"


async def add_points(user_id: str, delta: int) -> Tuple[int, str]:
    # changed code: ensure ObjectId when querying/updating users collection
    query_id = None
    try:
        query_id = ObjectId(user_id)
    except Exception:
        query_id = user_id

    user = await db.users.find_one({"_id": query_id}, {"points": 1, "badges": 1})
    if not user:
        return 0, "Bronze"

    new_points = int(user.get("points", 0)) + int(delta)
    if new_points < 0:
        new_points = 0
    new_badge = compute_badge(new_points)
    badges = set(user.get("badges", []))
    badges.add(new_badge)

    await db.users.update_one(
        {"_id": query_id},
        {"$set": {"points": new_points, "badge": new_badge, "badges": list(badges)}},
    )
    return new_points, new_badge
