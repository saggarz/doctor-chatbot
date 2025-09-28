from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Doctor(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialty = Column(String, index=True)
    department = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship to appointments
    appointments = relationship("Appointment", back_populates="doctor")

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship to appointments
    appointments = relationship("Appointment", back_populates="patient")

class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    patient_id = Column(Integer, ForeignKey("patients.id"))
    appointment_date = Column(DateTime)
    status = Column(String, default="scheduled")  # scheduled, completed, cancelled
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")

class DoctorAvailability(Base):
    __tablename__ = "doctor_availability"
    
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    day_of_week = Column(Integer)  # 0=Monday, 6=Sunday
    start_time = Column(String)  # Format: "09:00"
    end_time = Column(String)    # Format: "17:00"
    is_available = Column(Boolean, default=True)
    
    # Relationship
    doctor = relationship("Doctor")
