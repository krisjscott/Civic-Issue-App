from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth as auth_router
from .routers import issues as issues_router
from .routers import rewards as rewards_router
from .routers import users as users_router
from .database import connect_to_mongo, close_mongo_connection

app = FastAPI(title="Civic Issue Reporting & Rewards System", version="1.0.0")

@app.on_event("startup")
async def startup_db_client():
	await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
	await close_mongo_connection()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# Note: DB connection is handled lazily by routes to simplify demo startup

@app.get("/")
async def root():
	return {"message": "Civic API is running. See /docs for Swagger UI."}

@app.get("/healthz")
async def health():
	return {"status": "ok"}

app.include_router(auth_router.router, prefix="/auth", tags=["auth"])
app.include_router(issues_router.router, prefix="/issues", tags=["issues"])
app.include_router(rewards_router.router, prefix="/rewards", tags=["rewards"])
app.include_router(users_router.router, prefix="/users", tags=["users"])
