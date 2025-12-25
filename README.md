# GigIT 🚀  
**Mortgage approval, reimagined for the gig economy**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

---

## ✨ About GigIT

**GigIT** is an AI-powered verification platform designed to help banks and financial institutions **verify freelancers faster and more accurately** using their tax documents (such as 1099 forms).

Instead of slow, manual document reviews, GigIT automates income verification by analyzing submitted documents and generating a structured verification report for underwriters.

This reduces verification time **from days to hours** while improving fairness for gig workers.

---

## 💡 Inspiration

Freelancers are often excluded from traditional financial systems because verification processes are built for salaried employees.

GigIT was created to:
- Eliminate manual document review
- Speed up freelancer mortgage approvals
- Make banking more inclusive for independent workers

---

## ⚙️ What GigIT Does

- Gig workers submit income documents (e.g. 1099s)
- The backend processes PDFs and scanned images
- AI extracts and analyzes key financial signals
- A verification report is generated
- Banks make faster, more informed decisions

---

## 🖥️ Product Screenshots

### Landing Page
![Landing Page](./screenshots/landing.png)

### Mortgage Application Flow
![Mortgage Application](./screenshots/application.png)

### Bank Partner Login
![Bank Login](./screenshots/bank-login.png)

### Risk Configuration Dashboard
![Risk Dashboard](./screenshots/risk-dashboard.png)

> _Screenshots are from the local development build._

---

## 🛠️ How It Was Built

### Backend
- **FastAPI** (Python)
- PDF parsing with **PyPDF2**
- Image handling for scanned documents
- AI-powered document analysis (Gemini-ready)
- API testing with **Postman / curl**
- Local deployment using **Uvicorn**

### Frontend
- **React**
- Modular page and component architecture
- Interactive dashboards and multi-step flows
- Mock data for demos and local development

---

## 🧪 How to Run Locally

### 1️⃣ Clone the repository
git clone https://github.com/sansitamalhotra/GigIT.git
cd GigIT

2️⃣ Run the Backend

cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-multipart python-dotenv pillow PyPDF2 google-generativeai
Create a local .env file (this is not committed):

touch app/.env
Example .env:
env
GEMINI_API_KEY=""
Start the server:
uvicorn app.main:app --reload
Open API docs:
http://127.0.0.1:8000/docs

3️⃣ Run the Frontend

Open a new terminal:
cd frontend
npm install
npm start
Frontend runs at:

http://localhost:3000
The frontend can run independently using mock data if no API key is provided.

📂 Project Structure
text
Copy code
GigIT/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── main.py
│   └── tests/
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── subpages/
│   │   ├── services/
│   │   └── test_data/
└── README.md
🏆 Accomplishments
Built a full-stack AI-powered verification system

Automated freelancer income analysis

Designed a bank-facing risk configuration dashboard

Created a scalable FastAPI backend with a modern React frontend

🔮 Next Steps
Expand support for more document types

Add authentication and role-based access

Optimize AI processing speed

Deploy backend and frontend for a public demo

📄 License
This repository is view-only.
All rights reserved by Jemima Silaen, Vriti Dahiya, Sansita Malhotra.

No copying, redistribution, or derivative works are permitted without prior written consent.
See the LICENSE file for details.

