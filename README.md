# GigIT 🚀  
**Fast-track freelancer verification with AI-powered document analysis**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

---

## ✨ About GigIT

**GigIT** is an AI-powered verification platform designed to help banks 
and financial institutions **verify freelancers faster and more 
accurately** using their tax documents (such as 1099 forms).

Instead of slow, manual document reviews, GigIT uses modern AI techniques 
to extract and analyze relevant information, producing a structured 
verification report for underwriters to review.

This significantly reduces verification time **from days to hours**.

---

## 💡 Inspiration

Freelancers often face long delays when applying for financial products 
because traditional verification systems are built for salaried employees.

GigIT was created to:
- Reduce manual document review
- Speed up freelancer verification
- Make banking systems more inclusive for independent workers

---

## ⚙️ What It Does

- Users upload freelancer tax documents (e.g. 1099 forms)
- The backend processes PDFs or scanned images
- AI extracts and analyzes relevant financial information
- A verification report is generated for underwriters
- Banks make faster, more informed decisions

---

## 🛠 How It Was Built

### Backend
- **FastAPI** (Python)
- PDF processing with **PyPDF2**
- Image handling for scanned documents
- AI analysis using **Google Gemini**
- API testing with **Postman / curl**
- Local deployment with **Uvicorn**

### Frontend
- **React**
- Modular page & component structure
- Mock data for local development and demos

---

## 🧪 How to Run Locally

1️⃣ Clone the repository
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
Open API docs: http://127.0.0.1:8000/docs

3️⃣ Run the Frontend
Open a new terminal:
cd frontend
npm install
npm start
Frontend runs at: http://localhost:3000
The frontend can run independently using mock data if no API key is 
provided.

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
Built a fully functional document-processing API from scratch

Integrated AI-based document analysis

Designed specifically for freelancer verification workflows

Created a scalable backend with a modern frontend interface

🔮 Next Steps
Expand AI support for additional document types

Add authentication and role-based access

Improve AI processing speed and accuracy

Deploy backend and frontend for public demo access

📄 License
This repository is view-only.
All rights reserved by Jemima Silaen, Vriti Dahiya, Sansita Malhotra.

No copying, redistribution, or derivative works are permitted without 
prior written consent.
See the LICENSE file for details.
