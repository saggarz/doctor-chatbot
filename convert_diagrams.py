#!/usr/bin/env python3
"""
Script to convert Mermaid diagrams to images for Medium publication
"""

import requests
import base64
import os

def create_mermaid_image(mermaid_code, filename):
    """Convert Mermaid diagram to image using Mermaid.ink API"""
    
    # Encode the Mermaid code
    encoded = base64.b64encode(mermaid_code.encode('utf-8')).decode('utf-8')
    
    # Create the URL
    url = f"https://mermaid.ink/img/{encoded}"
    
    try:
        # Download the image
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"images/{filename}", 'wb') as f:
                f.write(response.content)
            print(f"✅ Created {filename}")
            return f"images/{filename}"
        else:
            print(f"❌ Failed to create {filename}")
            return None
    except Exception as e:
        print(f"❌ Error creating {filename}: {e}")
        return None

def main():
    """Create all diagram images"""
    
    # Create images directory
    os.makedirs("images", exist_ok=True)
    
    # Define diagrams
    diagrams = {
        "architecture": """
graph TB
    subgraph "Frontend (Vercel)"
        A[React App]
        B[Chat Interface]
        C[Doctor List]
        D[Appointment Booking]
    end
    
    subgraph "Backend (Render)"
        E[FastAPI Server]
        F[Chat Endpoint]
        G[Doctors API]
        H[Appointments API]
    end
    
    subgraph "Database (SQLite)"
        I[Doctors Table]
        J[Appointments Table]
        K[Patients Table]
        L[Availability Table]
    end
    
    subgraph "External Services"
        M[OpenAI API]
        N[GPT-3.5-turbo]
    end
    
    A --> E
    B --> F
    C --> G
    D --> H
    
    E --> I
    E --> J
    E --> K
    E --> L
    
    F --> M
    M --> N
        """,
        
        "chat_flow": """
sequenceDiagram
    participant U as User
    participant F as Frontend (React)
    participant B as Backend (FastAPI)
    participant D as Database (SQLite)
    participant O as OpenAI API

    U->>F: Types message: "I need orthopedic doctor"
    F->>B: POST /chat with message
    B->>O: Send chat completion request
    O-->>B: Response with function call
    B->>D: Query doctors by specialty
    D-->>B: Return orthopedic doctors
    B->>O: Send function result
    O-->>B: Final response with doctor list
    B-->>F: Return chat response
    F-->>U: Display doctor recommendations
        """,
        
        "database_schema": """
erDiagram
    Doctor ||--o{ DoctorAvailability : has
    Doctor ||--o{ Appointment : treats
    Patient ||--o{ Appointment : books
    
    Doctor {
        int id PK
        string name
        string specialty
        string department
    }
    
    DoctorAvailability {
        int id PK
        int doctor_id FK
        int day_of_week
        string start_time
        string end_time
        boolean is_available
    }
    
    Patient {
        int id PK
        string name
        string phone
        string email
    }
    
    Appointment {
        int id PK
        int doctor_id FK
        int patient_id FK
        datetime appointment_date
        string status
        string notes
    }
        """
    }
    
    print("🎨 Creating diagram images for Medium...")
    
    for name, code in diagrams.items():
        create_mermaid_image(code, f"{name}.png")
    
    print("\n📁 Images created in 'images/' directory")
    print("📝 You can now upload these to Medium when publishing your article")

if __name__ == "__main__":
    main()
