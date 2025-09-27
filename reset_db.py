from sqlalchemy.orm import Session
from database import SessionLocal, create_tables
from models import Doctor, DoctorAvailability, Patient, Appointment

def reset_database():
    """Reset database and reinitialize with new data"""
    print("Resetting database...")
    
    # Create tables (this will drop and recreate)
    create_tables()
    
    db = SessionLocal()
    
    try:
        # Clear existing data
        db.query(Appointment).delete()
        db.query(DoctorAvailability).delete()
        db.query(Patient).delete()
        db.query(Doctor).delete()
        db.commit()
        
        print("Database cleared successfully")
        print("Please restart the application to reinitialize with new data")
        
    except Exception as e:
        print(f"Error resetting database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    reset_database()
