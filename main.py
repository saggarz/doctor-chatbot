from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import uuid
import json
from datetime import datetime

from database import get_db, create_tables
from schemas import (
    ChatMessage, ChatResponse, Doctor, DoctorCreate, Patient, PatientCreate,
    Appointment, AppointmentCreate, DoctorAvailability, DoctorAvailabilityCreate
)
from models import Doctor as DoctorModel
from services import DoctorService, PatientService, AppointmentService, ChatbotService
from openai_service import OpenAIService

# Create tables
create_tables()

app = FastAPI(title="Doctor's Assistant Chatbot", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI service
openai_service = OpenAIService()

# Store chat sessions (in production, use Redis or database)
chat_sessions = {}

@app.get("/")
async def root():
    return {"message": "Doctor's Assistant Chatbot API"}

@app.get("/debug/doctors")
async def debug_doctors(db: Session = Depends(get_db)):
    """Debug endpoint to check what doctors are in the database"""
    doctors = db.query(DoctorModel).all()
    return {
        "count": len(doctors),
        "doctors": [
            {
                "id": doctor.id,
                "name": doctor.name,
                "specialty": doctor.specialty,
                "department": doctor.department
            }
            for doctor in doctors
        ]
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(message: ChatMessage, db: Session = Depends(get_db)):
    """Main chat endpoint for the chatbot"""
    try:
        # Generate or get session ID
        session_id = message.session_id or str(uuid.uuid4())
        
        # Initialize or get chat history
        if session_id not in chat_sessions:
            chat_sessions[session_id] = [
                {
                    "role": "system",
                    "content": """You are a helpful assistant for Super Clinic, a leading medical facility in India. You help patients book appointments with doctors across various specialties.
                    
                    You can:
                    - Check doctor availability
                    - Find doctors by specialty
                    - Book appointments
                    - Provide information about available doctors and their specialties
                    
                    Available specialties include: Cardiology, Orthopedics, Neurology, Dermatology, Pediatrics, Gynecology, General Medicine, Ophthalmology, ENT, Psychiatry, Gastroenterology, Urology, Pulmonology, Endocrinology, Nephrology, Oncology, and Rheumatology.
                    
                    Always be polite and helpful. When booking appointments, collect patient information like name and phone number.
                    
                    If a patient asks about symptoms, suggest appropriate specialists but note that you cannot provide medical advice. Always recommend consulting with a qualified doctor for proper diagnosis and treatment."""
                }
            ]
        
        # Limit chat history to prevent token overflow
        if len(chat_sessions[session_id]) > 20:
            # Keep system message and last 18 messages
            chat_sessions[session_id] = [chat_sessions[session_id][0]] + chat_sessions[session_id][-18:]
        
        # Add user message to history
        chat_sessions[session_id].append({
            "role": "user",
            "content": message.message
        })
        
        # Get response from OpenAI
        chatbot_service = ChatbotService(db)
        response = openai_service.get_chat_completion(chat_sessions[session_id])
        
        if not response["success"]:
            # If OpenAI fails, provide a fallback response
            fallback_response = "I apologize, but I'm experiencing some technical difficulties. Please try again in a moment, or contact our clinic directly for assistance."
            chat_sessions[session_id].append({
                "role": "assistant",
                "content": fallback_response
            })
            return ChatResponse(
                response=fallback_response,
                session_id=session_id
            )
        
        openai_message = response["response"]
        
        # Check if function was called
        if openai_message.function_call:
            try:
                function_name = openai_message.function_call.name
                function_args = json.loads(openai_message.function_call.arguments)
                
                # Process function call
                function_result = chatbot_service.process_function_call(function_name, function_args)
                
                # Add function call and result to chat history
                chat_sessions[session_id].append({
                    "role": "assistant",
                    "content": None,
                    "function_call": {
                        "name": function_name,
                        "arguments": openai_message.function_call.arguments
                    }
                })
                
                chat_sessions[session_id].append({
                    "role": "function",
                    "name": function_name,
                    "content": json.dumps(function_result)
                })
                
                # Get final response
                final_response = openai_service.get_simple_completion(chat_sessions[session_id])
                
                if final_response["success"]:
                    chat_sessions[session_id].append({
                        "role": "assistant",
                        "content": final_response["response"]
                    })
                    
                    return ChatResponse(
                        response=final_response["response"],
                        session_id=session_id,
                        function_called=function_name,
                        function_result=function_result
                    )
                else:
                    # If final response fails, provide a fallback
                    fallback_response = "I understand your request, but I'm having trouble processing it right now. Please try rephrasing your question or contact our clinic directly."
                    chat_sessions[session_id].append({
                        "role": "assistant",
                        "content": fallback_response
                    })
                    return ChatResponse(
                        response=fallback_response,
                        session_id=session_id
                    )
            except Exception as e:
                # If function calling fails, provide a fallback response
                fallback_response = "I understand your request, but I'm having some technical difficulties. Please try again or contact our clinic directly for assistance."
                chat_sessions[session_id].append({
                    "role": "assistant",
                    "content": fallback_response
                })
                return ChatResponse(
                    response=fallback_response,
                    session_id=session_id
                )
        else:
            # Simple response without function calling
            chat_sessions[session_id].append({
                "role": "assistant",
                "content": openai_message.content
            })
            
            return ChatResponse(
                response=openai_message.content,
                session_id=session_id
            )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Doctor management endpoints
@app.post("/doctors/", response_model=Doctor)
async def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    """Create a new doctor"""
    doctor_service = DoctorService(db)
    return doctor_service.create_doctor(doctor)

@app.get("/doctors/", response_model=List[Doctor])
async def get_doctors(db: Session = Depends(get_db)):
    """Get all doctors"""
    doctor_service = DoctorService(db)
    return doctor_service.get_all_doctors()

@app.get("/doctors/specialty/{specialty}", response_model=List[Doctor])
async def get_doctors_by_specialty(specialty: str, db: Session = Depends(get_db)):
    """Get doctors by specialty"""
    doctor_service = DoctorService(db)
    return doctor_service.get_doctors_by_specialty(specialty)

# Patient management endpoints
@app.post("/patients/", response_model=Patient)
async def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    """Create a new patient"""
    patient_service = PatientService(db)
    return patient_service.create_patient(patient)

@app.get("/patients/", response_model=List[Patient])
async def get_patients(db: Session = Depends(get_db)):
    """Get all patients"""
    patient_service = PatientService(db)
    return patient_service.db.query(Patient).all()

# Appointment management endpoints
@app.post("/appointments/", response_model=Appointment)
async def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    """Create a new appointment"""
    appointment_service = AppointmentService(db)
    return appointment_service.book_appointment(
        appointment.doctor_id,
        appointment.patient_id,
        appointment.appointment_date,
        appointment.notes
    )

@app.get("/appointments/", response_model=List[Appointment])
async def get_appointments(db: Session = Depends(get_db)):
    """Get all appointments"""
    appointment_service = AppointmentService(db)
    return appointment_service.db.query(Appointment).all()

# Doctor availability endpoints
@app.post("/doctor-availability/", response_model=DoctorAvailability)
async def create_doctor_availability(availability: DoctorAvailabilityCreate, db: Session = Depends(get_db)):
    """Create doctor availability"""
    db_availability = DoctorAvailability(**availability.dict())
    db.add(db_availability)
    db.commit()
    db.refresh(db_availability)
    return db_availability

@app.get("/doctor-availability/", response_model=List[DoctorAvailability])
async def get_doctor_availability(db: Session = Depends(get_db)):
    """Get all doctor availability"""
    return db.query(DoctorAvailability).all()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
