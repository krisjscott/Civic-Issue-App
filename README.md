🏙️ Civic Issue App

A modern civic engagement platform where citizens can report issues, track their status, and collaborate with local authorities. Built with React Native (frontend) and FastAPI + MongoDB (backend).

🚀 Features

📌 User Authentication (Signup/Login with JWT)

📝 Report Civic Issues with description, images, and location

📍 Location Integration (Google Maps / GPS support)

📊 Issue Tracking (track status: Submitted → In Progress → Resolved)

👥 Community Engagement (vote/comment on issues)

🔐 Secure backend with MongoDB Atlas

🛠️ Tech Stack

Frontend: React Native (Expo)
Backend: FastAPI (Python)
Database: MongoDB Atlas
Auth: JWT Authentication
Hosting: Local / Cloud deployment ready

📂 Project Structure
Civic-Issue-App/
├── backend/         # FastAPI server code
│   ├── main.py      # Entry point
│   ├── database.py  # MongoDB connection
│   └── routes/      # API routes
├── frontend/        # React Native mobile app
│   ├── App.js       # Main app entry
│   └── screens/     # UI screens
└── README.md

⚡ Getting Started
1. Clone the repo
git clone https://github.com/krisjscott/Civic-Issue-App.git
cd Civic-Issue-App

2. Backend Setup
cd backend
python -m venv .venv
. .venv/Scripts/activate    # Windows
source .venv/bin/activate   # Mac/Linux

pip install -r requirements.txt


Create a .env file:

MONGO_URI=mongodb+srv://<user>:<password>@cluster.mongodb.net
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256


Run the backend:

uvicorn main:app --reload


Visit http://127.0.0.1:8000/docs
 for Swagger UI.

3. Frontend Setup
cd frontend
npm install
npm start


Use Expo Go (mobile app) to scan the QR code and run on your phone.

✅ API Endpoints
Method	Endpoint	Description
POST	/auth/signup	Register new user
POST	/auth/login	Login user & get token
POST	/issues/	Submit new issue
GET	/issues/	Get all issues
GET	/issues/{id}	Get issue by ID
PUT	/issues/{id}	Update issue status
🤝 Contributing

Fork this repo

Create a branch: git checkout -b feature-name

Commit changes: git commit -m 'Added new feature'

Push branch: git push origin feature-name

Submit a Pull Request 🎉

📜 License

This project is licensed under the MIT License.
