from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
import os
import sys

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai_service import OpenAIService
from services import ChatbotService
from database import get_db
from schemas import ChatMessage, ChatResponse

app = FastAPI(title="Doctor's Assistant API")

# Initialize services
openai_service = OpenAIService()
chatbot_service = ChatbotService()

@app.get("/")
async def root():
    return {"message": "Doctor's Assistant API is running!"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(message: ChatMessage):
    """Handle chat messages with the AI assistant"""
    try:
        # Get database session
        db = next(get_db())
        
        # Process the chat message
        response = chatbot_service.process_message(
            message=message.message,
            db=db
        )
        
        return ChatResponse(
            response=response,
            success=True
        )
    except Exception as e:
        return ChatResponse(
            response=f"I apologize, but I'm experiencing technical difficulties. Please try again later. Error: {str(e)}",
            success=False
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "doctor-assistant-api"}
