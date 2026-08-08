Title: AI Chatbot with Custom Memory (Groq API + FastAPI)

Description: Custom memory feature, real-time chat, Python backend.

Features list:

- **Custom Memory**: Remembers previous conversations for context-aware responses
- **Real-time Chat**: Instant AI replies via Groq API integration
- **FastAPI Backend**: High-performance Python REST API with async support
- **Modern Frontend**: Responsive HTML/CSS/JS interface for seamless user experience
- **Secure API Keys**: Environment variables (.env) for Groq token protection
- **Easy Deployment**: requirements.txt & uvicorn for one-click setup
- **MIT Licensed**: Open-source, free for personal/commercial use with attribution


Installation: pip install -r requirements.txt, uvicorn app:app --reload.


## Live Demo

Frontend:
https://your-project.vercel.app

Backend:
https://your-backend.onrender.com/docs

---------------------------------------------------------------------------------------
# 🤖 AI Chatbot with Memory

An intelligent AI chatbot built using **FastAPI** and **LangChain** with conversation memory support. The chatbot provides context-aware responses by remembering previous interactions, creating a more natural conversational experience.

---

## 🚀 Live Demo

**Frontend:** https://your-vercel-url.vercel.app/

**Backend API:** https://your-render-url.onrender.com

**API Documentation (Swagger):** https://your-render-url.onrender.com/docs

---

## 📌 Features

- 💬 AI-powered chatbot
- 🧠 Conversation memory
- ⚡ FastAPI backend
- 🌐 Responsive HTML, CSS & JavaScript frontend
- 🔄 REST API integration
- ☁️ Deployed on Render & Vercel
- 🔐 Environment variable support for API keys
- 📖 Interactive Swagger API documentation

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- LangChain
- Uvicorn
- Python-dotenv

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- Render (Backend)
- Vercel (Frontend)
- GitHub

---

## 📂 Project Structure

```
AI_ChatBot_Memory/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   └── ...
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── styles.css
│   └── ...
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/himanshuDevCodes/Ai_ChatBot_Memory.git
```

### 2. Navigate to the Project

```bash
cd Ai_ChatBot_Memory
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file inside the `backend` folder.

Example:

```env
OPENAI_API_KEY=your_api_key
```

---

## ▶️ Run Backend

```bash
cd backend
python -m uvicorn app:app --reload
```

Backend will be available at:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

---

## ▶️ Run Frontend

Open

```
frontend/index.html
```

or use the **Live Server** extension in VS Code.

---

## 📡 API Endpoint

### Chat Endpoint

```
POST /chat
```

Example Request

```json
{
  "message": "Hello"
}
```

Example Response

```json
{
  "response": "Hi! How can I help you today?"
}
```

---

## ☁️ Deployment

### Backend

Hosted on **Render**

### Frontend

Hosted on **Vercel**

---

## 🔮 Future Enhancements

- User Authentication
- Persistent Chat History
- Database Integration
- Multiple LLM Support
- Voice Chat
- PDF Chat (RAG)
- Streaming Responses
- Docker Support

---

## 👨‍💻 Author

**Himanshu Kumar**

GitHub: https://github.com/himanshuDevCodes

LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
