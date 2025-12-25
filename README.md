# 🏦 GigIT

<div align="center">

![GigIT Banner](https://img.shields.io/badge/GigIT-AI%20Verification-4A90E2?style=for-the-badge&logo=bank&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini%202.5%20Pro-AI-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-18.3.1-61DAFB?style=for-the-badge&logo=react&logoColor=black)

### 💼 *Fast-track freelancer verification with AI-powered document analysis* 🚀

**Reducing freelancer bank approval from days to hours using generative AI**

[🏆 First Place - NewHacks 2025](#) • [📖 Documentation](#features) • [🐛 Report Bug](https://github.com/yourusername/gigit/issues)

</div>

---

## 📸 Screenshots

<div align="center">

### 🏠 Landing Page
![Landing Page](screenshots/landing.png)

### 🔐 Bank Login
![Bank Login](screenshots/bank-login.png)

### 📄 Application Interface
![Application](screenshots/application.png)

### ⚠️ Risk Configuration
![Risk Configuration](screenshots/risk-config.png)

</div>

---

## 💡 The Problem

Freelancers face **major delays** getting verified by banks because:
- ❌ Manual review of tax documents takes **days or weeks**
- ❌ Traditional verification systems don't support 1099 forms well
- ❌ Underwriters are overwhelmed with document processing
- ❌ Freelancers lose opportunities while waiting for approval

**GigIT solves this** by automating the verification process with AI.

---

## ✨ What GigIT Does

<div align="center">
```mermaid
graph LR
    A[👤 Freelancer] -->|Uploads 1099| B[📄 GigIT API]
    B -->|AI Analysis| C[🤖 Gemini 2.5 Pro]
    C -->|Generates Report| D[📊 Verification Report]
    D -->|Review| E[🏦 Bank Underwriter]
    E -->|✅ Approve| F[🎉 Verified!]
    
    style A fill:#E3F2FD
    style B fill:#BBDEFB
    style C fill:#90CAF9
    style D fill:#64B5F6
    style E fill:#42A5F5
    style F fill:#2196F3
```

</div>

### 🎯 Key Features

- 📤 **Document Upload** - Submit tax forms (1099, W-2, etc.) via API
- 🤖 **AI-Powered Analysis** - Gemini 2.5 Pro extracts and validates data
- ⚡ **Instant Reports** - Generate verification reports in seconds
- 🔍 **Underwriter Review** - Human-in-the-loop for final approval
- ⏱️ **Time Savings** - Reduce verification from **days to hours**
- 🔒 **Secure Processing** - Bank-grade document handling
- 📊 **Risk Scoring** - Automated risk assessment based on income patterns

---

## 🛠️ Tech Stack

### Backend
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-009688?style=flat-square&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-499848?style=flat-square)

### AI/ML
![Gemini](https://img.shields.io/badge/Gemini%202.5%20Pro-AI%20Model-4285F4?style=flat-square&logo=google)
![PyPDF2](https://img.shields.io/badge/PyPDF2-PDF%20Processing-DC143C?style=flat-square)

### Frontend
![React](https://img.shields.io/badge/React-18.3.1-61DAFB?style=flat-square&logo=react)
![Tailwind](https://img.shields.io/badge/Tailwind%20CSS-3.4.17-38B2AC?style=flat-square&logo=tailwind-css)
![Vite](https://img.shields.io/badge/Vite-6.0.1-646CFF?style=flat-square&logo=vite)

---

## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.11+
python --version

# Node.js 18+ (for frontend)
node --version
```

### Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/gigit.git
cd gigit
```

2️⃣ **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3️⃣ **Configure Environment**
```bash
# Create .env file in backend/
cp .env.example .env

# Add your Gemini API key
GEMINI_API_KEY=your_api_key_here
```

4️⃣ **Run the Backend**
```bash
uvicorn main:app --reload
```

5️⃣ **Frontend Setup** (Optional)
```bash
cd ../frontend
npm install
npm run dev
```

---

## 📡 API Documentation

### Upload Document for Verification

**POST** `/verify`
```bash
curl -X POST "http://localhost:8000/verify" \
  -F "file=@/path/to/1099.pdf" \
  -F "user_id=12345"
```

**Response:**
```json
{
  "status": "success",
  "verification_id": "v_abc123",
  "report": {
    "freelancer_name": "John Doe",
    "total_income": "$75,000",
    "tax_year": "2024",
    "risk_score": "LOW",
    "verification_status": "PENDING_REVIEW",
    "extracted_data": {
      "ein": "XX-XXXXXXX",
      "income_breakdown": {...}
    }
  }
}
```

### Get Verification Status

**GET** `/verify/{verification_id}`

curl "http://localhost:8000/verify/v_abc123"
```

---

## 🎨 Project Structure
```
gigit/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── ai_processor.py      # Gemini AI integration
│   ├── document_parser.py   # PDF/image processing
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables
│
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   └── App.jsx          # Main app
│   └── package.json
│
├── Mock Dataset/            # Test 1099 forms
├── screenshots/             # UI screenshots
└── README.md
```

---

## 🏆 Hackathon Achievement

<div align="center">

### 🥇 First Place - NewHacks 2025

Built in **24 hours** at University of Toronto's premier hackathon

**Team:** Jemima Silaen, Vriti Dahiya, Sansita Malhotra

</div>

---

## 🎯 What We Learned

### Technical Growth
- 🤖 **AI Integration** - First time working with Gemini 2.5 Pro's generative AI
- 📄 **Document Processing** - Learned to handle various PDF formats and scanned images
- ⚡ **FastAPI** - Built production-ready REST APIs with async processing
- 🔐 **Security** - Implemented secure file handling for sensitive documents

### Product Insights
- 💼 **Understanding User Needs** - Freelancers need faster, more accessible banking
- 🏦 **Industry Knowledge** - Learned about KYC (Know Your Customer) processes
- 🎨 **UX Design** - Created intuitive interfaces for both freelancers and banks

---

## 🚧 Challenges We Overcame

| Challenge | Solution |
|-----------|----------|
| 📄 **Varying PDF Formats** | Built robust parser supporting multiple 1099 variations |
| 🤖 **AI Accuracy** | Fine-tuned prompts and implemented validation checks |
| ⏱️ **Processing Speed** | Optimized AI calls and implemented caching |
| 🔒 **Data Security** | Implemented temporary file storage with auto-deletion |

---

## 🔮 Future Roadmap

### Phase 1: Enhanced Features
- [ ] 🌍 **International Forms** - Support for global tax documents
- [ ] 📊 **Analytics Dashboard** - Track verification trends and patterns
- [ ] 🔔 **Real-time Notifications** - Alert freelancers on status updates
- [ ] 🔐 **Authentication System** - OAuth2 for secure user access

### Phase 2: AI Improvements
- [ ] 🎯 **Multi-Model Support** - Add fallback AI models for redundancy
- [ ] 📈 **Confidence Scoring** - Show AI confidence in extracted data
- [ ] 🔍 **Fraud Detection** - Identify potential document tampering
- [ ] 💬 **Natural Language Queries** - Ask questions about documents

### Phase 3: Scale & Integration
- [ ] ☁️ **Cloud Deployment** - AWS/GCP production deployment
- [ ] 🏦 **Bank API Integration** - Direct integration with banking systems
- [ ] 📱 **Mobile App** - iOS/Android apps for freelancers
- [ ] 🌐 **Multi-tenant SaaS** - Support multiple banks on one platform

---

## 📄 License

**View-Only Repository**

All rights reserved by **Jemima Silaen**, **Vriti Dahiya**, and **Sansita Malhotra**.

No copying, redistribution, or derivative works are permitted without prior written consent. See [LICENSE](LICENSE) for details.

---

## 👥 Team

<div align="center">

| [Jemima Silaen](https://github.com/jemima) | [Vriti Dahiya](https://github.com/vriti) | [Sansita Malhotra](https://github.com/sansita) |
|:---:|:---:|:---:|
| Backend & AI | Frontend & UX | Full Stack |

</div>


<div align="center">

**Built with ❤️ at NewHacks 2025**

⭐ Star us on GitHub if you found this project interesting!

[![GitHub stars](https://img.shields.io/github/stars/yourusername/gigit?style=social)](https://github.com/yourusername/gigit)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/gigit?style=social)](https://github.com/yourusername/gigit/fork)

</div>
