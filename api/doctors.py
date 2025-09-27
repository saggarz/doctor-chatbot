from fastapi import FastAPI, HTTPException
from typing import List
import os
import sys

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services import DoctorService
from database import get_db
from schemas import Doctor

app = FastAPI(title="Doctors API")

# Initialize services
doctor_service = DoctorService()

@app.get("/", response_model=List[Doctor])
async def get_doctors():
    """Get all doctors"""
    try:
        db = next(get_db())
        doctors = doctor_service.get_all_doctors(db)
        return doctors
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching doctors: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "doctors-api"}
