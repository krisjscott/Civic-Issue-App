from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = None
db = None

# changed code: add simple settings object (used by utils/auth)
class Settings:
    mongo_uri: str = os.getenv("APP_MONGO_URI", "mongodb://localhost:27017")
    mongo_db: str = os.getenv("APP_MONGO_DB", "civic_control")
    jwt_secret: str = os.getenv("APP_JWT_SECRET", "CHANGE_ME_SUPER_SECRET")
    jwt_issuer: str = os.getenv("APP_JWT_ISSUER", "civic-control")
    jwt_exp_minutes: int = int(os.getenv("APP_JWT_EXP_MINUTES", "10080"))

settings = Settings()

async def connect_to_mongo():
    global client, db
    # changed code: use settings.mongo_uri / settings.mongo_db
    client = AsyncIOMotorClient(settings.mongo_uri)
    db = client.get_database(settings.mongo_db)
    await db.users.create_index("email", unique=True)
    await db.issues.create_index([("createdAt", -1)])
    await db.issues.create_index("reported_by")
    await db.issues.create_index("status")
    await db.issues.create_index("votes")

async def close_mongo_connection():
    global client
    if client:
        client.close()
