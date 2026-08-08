import os
from typing import List, Dict
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from rag.retriever import retrieve_context, vector_store_exists
load_dotenv()
import shutil
from config import UPLOAD_FOLDER
from rag.ingest import ingest

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")




if not GROQ_API_KEY:
    raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


client = Groq(api_key=GROQ_API_KEY)


class UserInput(BaseModel):
    message: str
    role: str = "user"
    conversation_id: str
    
class Conversation:
    def __init__(self):
        self.messages: List[Dict[str, str]] = [
            {"role": "system", "content": "You are a useful AI assistant."}
        ]
        self.active: bool = True

conversations: Dict[str, Conversation] = {}




def query_groq_api(conversation: Conversation) -> str:
    try:
        completion = client.chat.completions.create(
            model="groq/compound-mini",
            messages=conversation.messages,
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        
        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""
        
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error with Groq API Check : {str(e)}")


def get_or_create_conversation(conversation_id: str) -> Conversation:
    if conversation_id not in conversations:
        conversations[conversation_id] = Conversation()
    return conversations[conversation_id]




@app.post("/chat/")
async def chat(input: UserInput):
    conversation = get_or_create_conversation(input.conversation_id)

    if not conversation.active:
        raise HTTPException(
            status_code=400, 
            detail="The chat session has ended. Please start a new session."
        )
        
    try:
        
        # conversation.messages.append({
        #     "role": input.role,
        #     "content": input.message
        # })

        # Check whether a PDF has been uploaded
        if not vector_store_exists():
            raise HTTPException(
            status_code=400,
            detail="Please upload a PDF before asking questions."
        )
        context = retrieve_context(input.message)

        prompt = f"""
        You are a helpful AI assistant.

        Answer ONLY using the context below.

        If the answer is not found in the context,
        say:

        "I couldn't find that information in the uploaded document."

        Context:
        {context}

        Question:
        {input.message}
        """

        conversation.messages.append({
            "role": "user",
            "content": prompt
    })
        
        response = query_groq_api(conversation)
        
        conversation.messages.append({
            "role": "assistant",
            "content": response
        })
        
        return {
            "response": response,
            "conversation_id": input.conversation_id
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#rag endpoint
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF and automatically create its vector database.
    """

    # Allow only PDF files
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Save file
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Create vectors
    ingest(file_path)

    return {
        "message": "PDF uploaded successfully.",
        "filename": file.filename
    }
    #to test for all registered apis
#     print("\nRegistered Routes:")
# for route in app.routes:
#     print(route.path)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8005)