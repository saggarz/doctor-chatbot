from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class DoctorBase(BaseModel):
    name: str
    specialty: str
    department: str

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class PatientBase(BaseModel):
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class AppointmentBase(BaseModel):
    doctor_id: int
    patient_id: int
    appointment_date: datetime
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class DoctorAvailabilityBase(BaseModel):
    doctor_id: int
    day_of_week: int
    start_time: str
    end_time: str
    is_available: bool = True

class DoctorAvailabilityCreate(DoctorAvailabilityBase):
    pass

class DoctorAvailability(DoctorAvailabilityBase):
    id: int
    
    class Config:
        from_attributes = True

class ChatMessage(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    session_id: str
    function_called: Optional[str] = None
    function_result: Optional[dict] = None
