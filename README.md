# AI RAG Chatbot

A simple AI chatbot that uses **FastAPI** for the backend and a plain **HTML/CSS/JavaScript** frontend. The app supports PDF uploads, document retrieval via vector search, and Groq API-powered chat responses.

## Key Features

- 📄 Upload PDF documents
- 🧠 Retrieve document context for answers
- 🤖 Chat bot using the Groq API
- ⚡ FastAPI backend with CORS enabled
- 🌐 Frontend connects to backend at `http://localhost:8000`
- 🔐 Stores secrets in `.env`

## Project Structure

```
RAG_ChatBot/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── rag/
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── ingest.py
│   │   ├── loader.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   ├── chroma_db/
│   ├── data/
│   └── uploads/
└── frontend/
    ├── index.html
    ├── script.js
    ├── styles.css
    └── home.html
```

## Requirements

The backend dependencies are listed in `backend/requirements.txt`.

Main packages include:

- `fastapi`
- `uvicorn`
- `groq`
- `python-dotenv`
- `chromadb`
- `sentence-transformers`
- `pypdf`

## Setup

1. Open a terminal in the project root.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the environment:

Windows:

```powershell
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

4. Install backend dependencies:

```bash
cd backend
pip install -r requirements.txt
```

5. Create a `.env` file inside `backend/` with your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

## Run the App

From the `backend/` folder, start the FastAPI server:

```bash
python -m uvicorn app:app --reload
```

## Frontend Usage

Open the `frontend/index.html` file in your browser. If you want a local server, you can also use VS Code Live Server or any static file server to serve the `frontend/` folder.

Then use the chat interface to upload a PDF and send questions.

## API Endpoints

### Upload PDF

`POST /upload`

- Accepts a PDF file
- Saves it to `backend/uploads`
- Builds a vector store for retrieval

### Chat

`POST /chat/`

Request body example:

```json
{
  "message": "What is this document about?",
  "conversation_id": "001a"
}
```

Response example:

```json
{
  "response": "...assistant answer...",
  "conversation_id": "001a"
}
```

## Notes

- The frontend uses `http://localhost:8000` as the backend URL.
- A PDF must be uploaded before chat questions can use document context.
- The backend currently requires `GROQ_API_KEY` in `.env`.

## Troubleshooting

- If Uvicorn cannot import `app`, run it from the `backend/` folder or use:

```bash
python -m uvicorn backend.app:app --reload
```

- Make sure `python-dotenv` is installed and the `.env` file is present.

## License

MIT License.

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
