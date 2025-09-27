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
        
        # Create sample doctors with Indian names and comprehensive specialties
        doctors_data = [
            # Cardiology
            {
                "name": "Dr. Rajesh Kumar",
                "specialty": "Cardiology",
                "department": "Cardiology"
            },
            {
                "name": "Dr. Priya Sharma",
                "specialty": "Cardiology",
                "department": "Cardiology"
            },
            
            # Orthopedics
            {
                "name": "Dr. Amit Patel",
                "specialty": "Orthopedics",
                "department": "Orthopedics"
            },
            {
                "name": "Dr. Sunita Reddy",
                "specialty": "Orthopedics",
                "department": "Orthopedics"
            },
            
            # Neurology
            {
                "name": "Dr. Vikram Singh",
                "specialty": "Neurology",
                "department": "Neurology"
            },
            {
                "name": "Dr. Anjali Gupta",
                "specialty": "Neurology",
                "department": "Neurology"
            },
            
            # Dermatology
            {
                "name": "Dr. Ravi Verma",
                "specialty": "Dermatology",
                "department": "Dermatology"
            },
            {
                "name": "Dr. Meera Joshi",
                "specialty": "Dermatology",
                "department": "Dermatology"
            },
            
            # Pediatrics
            {
                "name": "Dr. Suresh Iyer",
                "specialty": "Pediatrics",
                "department": "Pediatrics"
            },
            {
                "name": "Dr. Kavita Nair",
                "specialty": "Pediatrics",
                "department": "Pediatrics"
            },
            
            # Gynecology
            {
                "name": "Dr. Deepak Agarwal",
                "specialty": "Gynecology",
                "department": "Gynecology"
            },
            {
                "name": "Dr. Rekha Desai",
                "specialty": "Gynecology",
                "department": "Gynecology"
            },
            
            # General Medicine
            {
                "name": "Dr. Arun Kumar",
                "specialty": "General Medicine",
                "department": "Internal Medicine"
            },
            {
                "name": "Dr. Shanti Devi",
                "specialty": "General Medicine",
                "department": "Internal Medicine"
            },
            
            # Ophthalmology
            {
                "name": "Dr. Mohan Lal",
                "specialty": "Ophthalmology",
                "department": "Ophthalmology"
            },
            {
                "name": "Dr. Geeta Singh",
                "specialty": "Ophthalmology",
                "department": "Ophthalmology"
            },
            
            # ENT
            {
                "name": "Dr. Ramesh Tiwari",
                "specialty": "ENT",
                "department": "ENT"
            },
            {
                "name": "Dr. Usha Menon",
                "specialty": "ENT",
                "department": "ENT"
            },
            
            # Psychiatry
            {
                "name": "Dr. Kailash Pandey",
                "specialty": "Psychiatry",
                "department": "Psychiatry"
            },
            {
                "name": "Dr. Indira Rao",
                "specialty": "Psychiatry",
                "department": "Psychiatry"
            },
            
            # Gastroenterology
            {
                "name": "Dr. Suresh Malhotra",
                "specialty": "Gastroenterology",
                "department": "Gastroenterology"
            },
            {
                "name": "Dr. Poonam Khanna",
                "specialty": "Gastroenterology",
                "department": "Gastroenterology"
            },
            
            # Urology
            {
                "name": "Dr. Harish Chopra",
                "specialty": "Urology",
                "department": "Urology"
            },
            {
                "name": "Dr. Neeta Kapoor",
                "specialty": "Urology",
                "department": "Urology"
            },
            
            # Pulmonology
            {
                "name": "Dr. Ashok Mehta",
                "specialty": "Pulmonology",
                "department": "Pulmonology"
            },
            {
                "name": "Dr. Radha Krishnan",
                "specialty": "Pulmonology",
                "department": "Pulmonology"
            },
            
            # Endocrinology
            {
                "name": "Dr. Gopal Das",
                "specialty": "Endocrinology",
                "department": "Endocrinology"
            },
            {
                "name": "Dr. Leela Venkatesh",
                "specialty": "Endocrinology",
                "department": "Endocrinology"
            },
            
            # Nephrology
            {
                "name": "Dr. Ravi Shankar",
                "specialty": "Nephrology",
                "department": "Nephrology"
            },
            {
                "name": "Dr. Sarita Agarwal",
                "specialty": "Nephrology",
                "department": "Nephrology"
            },
            
            # Oncology
            {
                "name": "Dr. Vijay Kumar",
                "specialty": "Oncology",
                "department": "Oncology"
            },
            {
                "name": "Dr. Kamala Devi",
                "specialty": "Oncology",
                "department": "Oncology"
            },
            
            # Rheumatology
            {
                "name": "Dr. Prakash Jain",
                "specialty": "Rheumatology",
                "department": "Rheumatology"
            },
            {
                "name": "Dr. Sunita Bhatia",
                "specialty": "Rheumatology",
                "department": "Rheumatology"
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
