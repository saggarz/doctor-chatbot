from sqlalchemy.orm import Session
from database import SessionLocal, create_tables
from models import Doctor, DoctorAvailability, Patient, Appointment
from datetime import datetime, timedelta

def init_database():
    """Initialize database with sample data"""
    create_tables()
    
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(Doctor).first():
            print("Database already initialized")
            return
        
        # Create sample doctors
        doctors_data = [
            {
                "name": "Dr. Sarah Johnson",
                "specialty": "Cardiology",
                "department": "Internal Medicine"
            },
            {
                "name": "Dr. Michael Chen",
                "specialty": "Orthopedics",
                "department": "Surgery"
            },
            {
                "name": "Dr. Emily Davis",
                "specialty": "Dermatology",
                "department": "Dermatology"
            },
            {
                "name": "Dr. Robert Wilson",
                "specialty": "Orthopedics",
                "department": "Surgery"
            },
            {
                "name": "Dr. Lisa Brown",
                "specialty": "General Medicine",
                "department": "Internal Medicine"
            }
        ]
        
        doctors = []
        for doctor_data in doctors_data:
            doctor = Doctor(**doctor_data)
            db.add(doctor)
            db.flush()  # Get the ID
            doctors.append(doctor)
        
        # Create doctor availability
        availability_data = []
        for doctor in doctors:
            # Each doctor is available Monday to Friday, 9 AM to 5 PM
            for day in range(5):  # Monday to Friday
                availability_data.append({
                    "doctor_id": doctor.id,
                    "day_of_week": day,
                    "start_time": "09:00",
                    "end_time": "17:00",
                    "is_available": True
                })
        
        for avail_data in availability_data:
            availability = DoctorAvailability(**avail_data)
            db.add(availability)
        
        # Create sample patients
        patients_data = [
            {
                "name": "John Smith",
                "phone": "+1234567890",
                "email": "john.smith@email.com"
            },
            {
                "name": "Jane Doe",
                "phone": "+1234567891",
                "email": "jane.doe@email.com"
            }
        ]
        
        patients = []
        for patient_data in patients_data:
            patient = Patient(**patient_data)
            db.add(patient)
            db.flush()
            patients.append(patient)
        
        # Create sample appointments
        tomorrow = datetime.now() + timedelta(days=1)
        appointments_data = [
            {
                "doctor_id": doctors[0].id,  # Dr. Sarah Johnson
                "patient_id": patients[0].id,
                "appointment_date": tomorrow.replace(hour=10, minute=0, second=0, microsecond=0),
                "status": "scheduled",
                "notes": "Regular checkup"
            },
            {
                "doctor_id": doctors[1].id,  # Dr. Michael Chen
                "patient_id": patients[1].id,
                "appointment_date": tomorrow.replace(hour=14, minute=30, second=0, microsecond=0),
                "status": "scheduled",
                "notes": "Knee pain consultation"
            }
        ]
        
        for appointment_data in appointments_data:
            appointment = Appointment(**appointment_data)
            db.add(appointment)
        
        db.commit()
        print("Database initialized successfully with sample data")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_database()
