from sqlalchemy.orm import Session
from models import Doctor, Patient, Appointment, DoctorAvailability
from schemas import DoctorCreate, PatientCreate, AppointmentCreate, DoctorAvailabilityCreate
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
import re

class DoctorService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_doctor(self, doctor: DoctorCreate) -> Doctor:
        db_doctor = Doctor(**doctor.dict())
        self.db.add(db_doctor)
        self.db.commit()
        self.db.refresh(db_doctor)
        return db_doctor
    
    def get_doctor_by_name(self, name: str) -> Optional[Doctor]:
        return self.db.query(Doctor).filter(Doctor.name.ilike(f"%{name}%")).first()
    
    def get_doctors_by_specialty(self, specialty: str) -> List[Doctor]:
        return self.db.query(Doctor).filter(Doctor.specialty.ilike(f"%{specialty}%")).all()
    
    def get_all_doctors(self) -> List[Doctor]:
        return self.db.query(Doctor).all()
    
    def check_doctor_availability(self, doctor_name: str, date: str, time: str) -> Dict[str, Any]:
        """Check if a doctor is available at a specific date and time"""
        doctor = self.get_doctor_by_name(doctor_name)
        if not doctor:
            return {"available": False, "reason": "Doctor not found"}
        
        # Parse date and time
        try:
            appointment_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            return {"available": False, "reason": "Invalid date or time format"}
        
        # Check if there's already an appointment at this time
        existing_appointment = self.db.query(Appointment).filter(
            Appointment.doctor_id == doctor.id,
            Appointment.appointment_date == appointment_datetime,
            Appointment.status == "scheduled"
        ).first()
        
        if existing_appointment:
            return {"available": False, "reason": "Doctor already has an appointment at this time"}
        
        # Check doctor's general availability (day of week)
        day_of_week = appointment_datetime.weekday()
        availability = self.db.query(DoctorAvailability).filter(
            DoctorAvailability.doctor_id == doctor.id,
            DoctorAvailability.day_of_week == day_of_week,
            DoctorAvailability.is_available == True
        ).first()
        
        if not availability:
            return {"available": False, "reason": "Doctor not available on this day"}
        
        # Check if time is within working hours
        appointment_time = appointment_datetime.time()
        start_time = datetime.strptime(availability.start_time, "%H:%M").time()
        end_time = datetime.strptime(availability.end_time, "%H:%M").time()
        
        if not (start_time <= appointment_time <= end_time):
            return {"available": False, "reason": "Time is outside doctor's working hours"}
        
        return {"available": True, "doctor": doctor}
    
    def get_available_doctors(self, date: str, time: str) -> List[Dict[str, Any]]:
        """Get all doctors available at a specific date and time"""
        available_doctors = []
        doctors = self.get_all_doctors()
        
        for doctor in doctors:
            availability = self.check_doctor_availability(doctor.name, date, time)
            if availability["available"]:
                available_doctors.append({
                    "id": doctor.id,
                    "name": doctor.name,
                    "specialty": doctor.specialty,
                    "department": doctor.department
                })
        
        return available_doctors

class PatientService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_patient(self, patient: PatientCreate) -> Patient:
        db_patient = Patient(**patient.dict())
        self.db.add(db_patient)
        self.db.commit()
        self.db.refresh(db_patient)
        return db_patient
    
    def get_patient_by_phone(self, phone: str) -> Optional[Patient]:
        return self.db.query(Patient).filter(Patient.phone == phone).first()

class AppointmentService:
    def __init__(self, db: Session):
        self.db = db
        self.doctor_service = DoctorService(db)
        self.patient_service = PatientService(db)
    
    def book_appointment(self, doctor_name: str, patient_name: str, patient_phone: str, 
                        appointment_date: str, appointment_time: str, notes: str = None) -> Dict[str, Any]:
        """Book an appointment"""
        # Check doctor availability
        availability = self.doctor_service.check_doctor_availability(doctor_name, appointment_date, appointment_time)
        if not availability["available"]:
            return {"success": False, "message": availability["reason"]}
        
        doctor = availability["doctor"]
        
        # Find or create patient
        patient = self.patient_service.get_patient_by_phone(patient_phone)
        if not patient:
            patient = self.patient_service.create_patient(PatientCreate(
                name=patient_name,
                phone=patient_phone
            ))
        
        # Create appointment
        appointment_datetime = datetime.strptime(f"{appointment_date} {appointment_time}", "%Y-%m-%d %H:%M")
        appointment = Appointment(
            doctor_id=doctor.id,
            patient_id=patient.id,
            appointment_date=appointment_datetime,
            notes=notes,
            status="scheduled"
        )
        
        self.db.add(appointment)
        self.db.commit()
        self.db.refresh(appointment)
        
        return {
            "success": True,
            "message": "Appointment booked successfully",
            "appointment_id": appointment.id,
            "doctor": doctor.name,
            "patient": patient.name,
            "date": appointment_date,
            "time": appointment_time
        }
    
    def get_appointments_by_doctor(self, doctor_id: int) -> List[Appointment]:
        return self.db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()

class ChatbotService:
    def __init__(self, db: Session):
        self.db = db
        self.doctor_service = DoctorService(db)
        self.appointment_service = AppointmentService(db)
    
    def process_function_call(self, function_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Process function calls from the chatbot"""
        try:
            if function_name == "check_doctor_availability":
                return self.doctor_service.check_doctor_availability(
                    arguments["doctor_name"],
                    arguments["date"],
                    arguments["time"]
                )
            
            elif function_name == "find_doctors_by_specialty":
                doctors = self.doctor_service.get_doctors_by_specialty(arguments["specialty"])
                return {
                    "doctors": [{"name": d.name, "specialty": d.specialty, "department": d.department} for d in doctors]
                }
            
            elif function_name == "book_appointment":
                return self.appointment_service.book_appointment(
                    arguments["doctor_name"],
                    arguments["patient_name"],
                    arguments.get("patient_phone", ""),
                    arguments["appointment_date"],
                    arguments["appointment_time"],
                    arguments.get("notes", "")
                )
            
            elif function_name == "get_available_doctors":
                doctors = self.doctor_service.get_available_doctors(
                    arguments["date"],
                    arguments["time"]
                )
                return {"available_doctors": doctors}
            
            else:
                return {"error": f"Unknown function: {function_name}"}
        
        except Exception as e:
            return {"error": str(e)}
