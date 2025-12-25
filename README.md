# 🏦 GigIT

<div align="center">

![GigIT Banner](https://img.shields.io/badge/GigIT-AI%20Verification-4A90E2?style=for-the-badge&logo=bank&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini%202.5%20Pro-AI-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-18.3.1-61DAFB?style=for-the-badge&logo=react&logoColor=black)

### 💼 *Mortgage approval, reimagined for the gig economy* 🚀

**Full-stack AI platform reducing freelancer verification from days to hours**

[🏆 First Place - NewHacks 2025](#) • [📖 Documentation](#-tech-stack)

</div>

---

## 📸 Screenshots

<div align="center">

### 🏠 Landing Page
![Landing Page](screenshots/landing.png)

### 📄 Application Flow
![Application](screenshots/application.png)

### 🔐 Bank Partner Login
![Bank Login](screenshots/bank-login.png)

### ⚙️ Risk Configuration
![Risk Configuration](screenshots/risk-config.png)

</div>

---

## 🚀 Tech Stack

**Backend:** FastAPI (Python)  
**Frontend:** React  
**AI / Document Analysis:** Gemini-powered (API-ready)  
**PDF Processing:** PyPDF2  
**Local Dev:** Uvicorn, npm  
**Data:** Mock datasets for demos

---

## ✨ About GigIT

Traditional mortgage and loan verification systems are built for salaried employees. **Gig workers often face delays or rejections** simply because their income is harder to verify.

**GigIT solves this by:**
- 📤 Automating income verification from tax documents
- 🤖 Extracting structured financial data using AI
- 📊 Generating clear verification reports for banks
- ⚡ Allowing underwriters to make faster, fairer decisions

---

## 💡 Inspiration

Freelancers are consistently underserved by traditional banking workflows.

**GigIT was created to:**
- ❌ Eliminate slow, manual document reviews
- ✅ Speed up mortgage and loan approvals
- 💼 Support independent workers with modern verification tools

---

## ⚙️ What GigIT Does

1. 👤 Gig workers submit income documents (e.g. 1099s)
2. 📄 The backend processes PDFs and scanned images
3. 🤖 AI extracts key financial information
4. 📊 A verification report is generated
5. 🏦 Banks review results and approve applications faster

---

## 🛠️ How It Was Built

### Backend
- FastAPI (Python)
- PDF parsing with PyPDF2
- Image handling for scanned documents
- AI-ready document analysis (Gemini compatible)
- API testing with Postman / curl
- Local deployment using Uvicorn

### Frontend
- React
- Modular page and component structure
- Multi-step application flows
- Interactive dashboards for bank partners
- Mock data for demos and local development

---

## 🧪 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sansitamalhotra/GigIT.git
cd GigIT
```

### 2️⃣ Run the Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

**Install dependencies:**
```bash
pip install fastapi uvicorn python-multipart python-dotenv pillow PyPDF2 google-generativeai
```

**Create a local `.env` file:**
```bash
touch app/.env
```

**Example `.env`:**
```
GEMINI_API_KEY=""
```

**Start the backend server:**
```bash
uvicorn app.main:app --reload
```

Backend runs at: `http://127.0.0.1:8000`  
API docs available at: `http://127.0.0.1:8000/docs`

### 3️⃣ Run the Frontend

**Open a new terminal:**
```bash
cd frontend
npm install
npm start
```

Frontend runs at: `http://localhost:3000`

The frontend can run independently using mock data if no API key is provided.

---

## 📂 Project Structure
```
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
├── screenshots/
│   ├── landing.png
│   ├── application.png
│   ├── bank-login.png
│   └── risk-config.png
├── Mock Dataset/
├── README.md
└── LICENSE
```

---

## 🏆 Accomplishments

- ✅ Built a full-stack AI-powered verification system
- 🤖 Automated freelancer income analysis
- 📊 Designed a bank-facing risk configuration dashboard
- 🚀 Created a scalable FastAPI backend with a modern React frontend

---

## 🔮 Next Steps

- [ ] 🌍 Expand support for more document types
- [ ] 🔐 Add authentication and role-based access
- [ ] ⚡ Improve AI processing speed and accuracy
- [ ] ☁️ Deploy backend and frontend for a public demo

---

## 📄 License

**View-Only Repository**

All rights reserved by **Jemima Silaen**, **Vriti Dahiya**, and **Sansita Malhotra**.

No copying, redistribution, or derivative works are permitted without prior written consent.

See the [LICENSE](LICENSE) file for details.
