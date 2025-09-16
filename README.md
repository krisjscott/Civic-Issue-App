# 🏙️ Civic Issue App

A mobile + backend platform that lets citizens report civic issues, track their resolution, and collaborate with local authorities. Built for Jharkhand & Bihar communities. SIH 2025 project  


## 🚀 Features

- **User Authentication** (Signup / Login with JWT)  
- **Report Issues** with title, description, category, image, and location  
- **Track Issue Status**: Pending → In Progress → Resolved  
- **Upvotes & Community Engagement** — issues can be upvoted to show priority  
- **Rewards System** — users earn points for reporting, upvotes, and resolved issues, redeemable for vouchers  
- **Secure Backend** using MongoDB Atlas  

---

## 🧰 Tech Stack

| Component        | Technology                          |
|------------------|--------------------------------------|
| Frontend         | React Native (Expo)                 |
| Backend          | FastAPI (Python)                    |
| Database         | MongoDB Atlas                       |
| Auth             | JWT (JSON Web Tokens)               |
| Hosting / DevOps | Local, easily deployed to cloud     |

---

## 📁 Project Structure

```

Civic-Issue-App/
├── backend/          # FastAPI server
│   ├── main.py       # Entry point
│   ├── database.py   # MongoDB connection & indexes
│   ├── models/       # Pydantic models
│   ├── routers/      # API route modules
│   └── utils/        # Helpers like auth, points logic
├── frontend/         # React Native app
│   ├── App.js        # Main entry file
│   └── screens/      # UI screen components
└── README.md         # This file

````

---

## 🔧 Getting Started

### Prerequisites

- Python 3.10+  
- Node.js & npm / Yarn  
- MongoDB Atlas account  

---

### Backend Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/krisjscott/Civic-Issue-App.git
   cd Civic-Issue-App/backend
``

2. **Create virtual environment and activate it**

   * **Windows (PowerShell)**:

     ```powershell
     python -m venv .venv
     . .venv\Scripts\Activate.ps1
     ```
   * **Mac / Linux**:

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install backend dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables** (create `.env` file in `backend/`)

   ```ini
   APP_MONGO_URI="mongodb+srv://hackathon_user:YourPassword@krish.donzfdl.mongodb.net/civic_control?retryWrites=true&w=majority&appName=CivicIssueApp"
   APP_MONGO_DB="civic_control"
   APP_JWT_SECRET="your_jwt_secret_here"
   APP_JWT_ISSUER="civic_control"
   APP_JWT_EXP_MINUTES=10080  # 7 days
   ```

5. **Run the backend**

   ```bash
   uvicorn main:app --reload
   ```

6. Open Swagger docs at:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### Frontend Setup (coming soon)

> *Note: Add instructions once the React Native frontend is ready.*

1. Go into `frontend/`

   ```bash
   cd ../frontend
   ```

2. Install dependencies

   ```bash
   npm install
   npm start
   ```

3. Use Expo Go (iOS / Android) to preview app on your phone.

---

### 🎯 API Endpoints (Examples)

| Method  | Endpoint              | Description                     |
| ------- | --------------------- | ------------------------------- |
| `POST`  | `/auth/signup`        | Register a new user             |
| `POST`  | `/auth/login`         | Log in and get JWT token        |
| `POST`  | `/issues/`            | Report a new civic issue        |
| `GET`   | `/issues/mine`        | Get issues submitted by me      |
| `GET`   | `/issues/`            | Admin: fetch all issues         |
| `POST`  | `/issues/{id}/upvote` | Upvote a specific issue         |
| `PATCH` | `/issues/{id}/status` | Admin: update an issue’s status |
| `POST`  | `/rewards/redeem`     | Redeem points for a voucher     |

---

### 💡 Contribution & Ideas

We welcome contributions, suggestions, and improvements.

* If you find bugs → create an issue
* Want to add a feature? Fork, build, and send a pull request
* Some future ideas: heat maps, multilingual support, SMS fallback, better mobile UI

---

### 📜 License

Open source under the [MIT License](LICENSE).

---

### 🚀 GitHub About (Tagline)

> A citizen-driven platform to report, track, and resolve civic issues — built with FastAPI, React Native, and MongoDB Atlas.

```
