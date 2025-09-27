# Doctor's Assistant Chatbot - Sequence Diagrams

## 1. User Chat Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend (React)
    participant B as Backend (FastAPI)
    participant D as Database (SQLite)
    participant O as OpenAI API

    Note over U,O: User starts chat session
    
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
    
    Note over U,O: User books appointment
    
    U->>F: "Book with Dr. Amit Patel"
    F->>B: POST /chat with booking request
    B->>O: Process booking request
    O-->>B: Function call for booking
    B->>D: Create appointment record
    D-->>B: Confirm appointment created
    B-->>F: Booking confirmation
    F-->>U: Show booking success
```

## 2. Doctor Search Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend (React)
    participant B as Backend (FastAPI)
    participant D as Database (SQLite)

    U->>F: Clicks "Find Doctors"
    F->>B: GET /doctors/
    B->>D: Query all doctors
    D-->>B: Return doctor list
    B-->>F: Return doctors data
    F-->>U: Display doctor cards

    Note over U,D: User filters by specialty
    
    U->>F: Selects "Cardiology" filter
    F->>B: GET /doctors/specialty/cardiology
    B->>D: Query doctors by specialty
    D-->>B: Return cardiology doctors
    B-->>F: Return filtered doctors
    F-->>U: Display filtered results
```

## 3. Appointment Booking Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend (React)
    participant B as Backend (FastAPI)
    participant D as Database (SQLite)

    U->>F: Clicks "Book Appointment"
    F->>B: GET /doctors/ (to show available doctors)
    B->>D: Query doctors
    D-->>B: Return doctors
    B-->>F: Return doctors list
    F-->>U: Show doctor selection

    U->>F: Selects doctor and fills form
    F->>B: POST /appointments/ with booking data
    B->>D: Create appointment record
    D-->>B: Confirm appointment created
    B-->>F: Return booking confirmation
    F-->>U: Show booking success message
```

## 4. System Architecture Flow

```mermaid
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
    
    style A fill:#e1f5fe
    style E fill:#f3e5f5
    style I fill:#e8f5e8
    style M fill:#fff3e0
```

## 5. Error Handling Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend (React)
    participant B as Backend (FastAPI)
    participant O as OpenAI API

    U->>F: Sends message
    F->>B: POST /chat
    B->>O: Request to OpenAI
    
    alt OpenAI Success
        O-->>B: Response with function call
        B-->>F: Success response
        F-->>U: Display AI response
    else OpenAI Failure
        O-->>B: Error response
        B-->>F: Fallback response
        F-->>U: "I'm having technical difficulties"
    else Network Error
        B-->>F: Network error
        F-->>U: "Please check your connection"
    end
```

## 6. Database Schema Relationships

```mermaid
erDiagram
    Doctor ||--o{ DoctorAvailability : has
    Doctor ||--o{ Appointment : treats
    Patient ||--o{ Appointment : books
    
    Doctor {
        int id PK
        string name
        string specialty
        string department
        datetime created_at
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
        datetime created_at
    }
    
    Appointment {
        int id PK
        int doctor_id FK
        int patient_id FK
        datetime appointment_date
        string status
        string notes
        datetime created_at
    }
```

## 7. Deployment Flow

```mermaid
sequenceDiagram
    participant D as Developer
    participant G as GitHub
    participant V as Vercel
    participant R as Render
    participant U as User

    D->>G: Push code changes
    G->>V: Trigger frontend deployment
    G->>R: Trigger backend deployment
    
    V->>V: Build React app
    V->>V: Deploy to CDN
    V-->>U: Frontend available
    
    R->>R: Install Python dependencies
    R->>R: Initialize database
    R->>R: Start FastAPI server
    R-->>U: Backend available
    
    U->>V: Access frontend
    V->>R: API calls to backend
    R-->>V: Return data
    V-->>U: Display results
```

## 8. User Journey Flow

```mermaid
journey
    title User Journey: Booking a Doctor Appointment
    
    section Discovery
      Visit website: 5: User
      Browse doctors: 4: User
      Read doctor profiles: 3: User
    
    section Selection
      Filter by specialty: 4: User
      Compare doctors: 3: User
      Select preferred doctor: 5: User
    
    section Booking
      Fill appointment form: 3: User
      Select date and time: 4: User
      Provide contact details: 3: User
      Confirm booking: 5: User
    
    section Confirmation
      Receive confirmation: 5: User
      Save appointment details: 4: User
```

## 9. API Request/Response Flow

```mermaid
sequenceDiagram
    participant C as Client
    participant F as Frontend
    participant B as Backend
    participant D as Database
    participant O as OpenAI

    Note over C,O: Chat Request Flow
    
    C->>F: User types message
    F->>B: POST /chat {"message": "I need a cardiologist"}
    
    B->>O: OpenAI API call with function definitions
    O-->>B: Response with function_call: "find_doctors_by_specialty"
    
    B->>D: SELECT * FROM doctors WHERE specialty = 'Cardiology'
    D-->>B: Return cardiology doctors
    
    B->>O: Send function result to OpenAI
    O-->>B: Final response with doctor recommendations
    
    B-->>F: {"response": "Here are cardiologists...", "success": true}
    F-->>C: Display doctor recommendations
```

## 10. Error Recovery Flow

```mermaid
flowchart TD
    A[User Request] --> B{API Available?}
    B -->|Yes| C[Process Request]
    B -->|No| D[Show Error Message]
    
    C --> E{OpenAI Available?}
    E -->|Yes| F[Get AI Response]
    E -->|No| G[Return Fallback Response]
    
    F --> H{Function Call Required?}
    H -->|Yes| I[Execute Function]
    H -->|No| J[Return AI Response]
    
    I --> K{Database Available?}
    K -->|Yes| L[Query Database]
    K -->|No| M[Return Error Message]
    
    L --> N[Return Function Result]
    N --> O[Get Final AI Response]
    O --> P[Return to User]
    
    G --> Q[Log Error]
    M --> Q
    Q --> R[Monitor for Recovery]
    R --> A
    
    style A fill:#e1f5fe
    style P fill:#e8f5e8
    style Q fill:#ffebee
```
