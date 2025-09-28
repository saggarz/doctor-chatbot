from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Doctor's Assistant API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Doctor's Assistant API is running!", "status": "healthy"}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "doctor-assistant-api"}

@app.post("/chat")
async def chat(message: dict):
    """Simple chat endpoint"""
    try:
        user_message = message.get("message", "")
        
        # Simple response for now
        response = f"I received your message: '{user_message}'. The AI chat functionality will be available once we set up the OpenAI API key."
        
        return {
            "response": response,
            "success": True
        }
    except Exception as e:
        return {
            "response": f"Error: {str(e)}",
            "success": False
        }

@app.get("/doctors")
async def get_doctors():
    """Get doctors list"""
    try:
        # Sample doctors data
        doctors = [
            {
                "id": 1,
                "name": "Dr. Sarah Johnson",
                "specialty": "Cardiology",
                "experience": "10 years",
                "rating": 4.8,
                "available": True
            },
            {
                "id": 2,
                "name": "Dr. Michael Chen",
                "specialty": "Neurology", 
                "experience": "8 years",
                "rating": 4.9,
                "available": True
            },
            {
                "id": 3,
                "name": "Dr. Emily Davis",
                "specialty": "Pediatrics",
                "experience": "12 years", 
                "rating": 4.7,
                "available": False
            }
        ]
        
        return {"doctors": doctors, "success": True}
    except Exception as e:
        return {"error": str(e), "success": False}

# This is the main handler for Vercel
handler = app
