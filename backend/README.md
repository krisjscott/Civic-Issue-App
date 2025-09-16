## Civic Issue Reporting & Rewards System (FastAPI + MongoDB)

### Setup (Windows PowerShell)
1. Create virtual environment and install deps
```
python -m venv .venv
. .venv/Scripts/Activate.ps1
pip install -r backend/requirements.txt
```

2. Configure environment in `backend/.env`
```
APP_MONGO_URI=mongodb://localhost:27017
APP_MONGO_DB=civic_control
APP_JWT_SECRET=CHANGE_ME_SUPER_SECRET
APP_JWT_ISSUER=civic-control
APP_JWT_EXP_MINUTES=10080
```

3. Run the API server
```
uvicorn backend.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for Swagger UI.

### API Summary
- POST `/auth/signup`
- POST `/auth/login`
- GET `/auth/me`
- POST `/issues/`
- GET `/issues/mine`
- GET `/issues/` (admin)
- PATCH `/issues/{id}/status?status=pending|in-progress|resolved` (admin)
- POST `/issues/{id}/upvote`
- GET `/users/me`
- POST `/rewards/redeem`

### Notes
- Make a user admin by updating `role` in the `users` collection.
- CORS is open for demo; restrict in production.
