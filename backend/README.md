# Doctor's Assistant Chatbot - Backend

FastAPI backend for the Doctor's Assistant Chatbot application.

## 🚀 Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Start the server
python main.py
```

### Production Deployment
The backend is deployed on Render at: https://doctor-chatbot-api-5v9h.onrender.com

## 📁 Project Structure

```
backend/
├── main.py              # FastAPI application entry point
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic schemas for API
├── services.py          # Business logic and OpenAI integration
├── openai_service.py    # OpenAI API service
├── database.py          # Database connection and session management
├── config.py            # Configuration settings
├── init_db.py           # Database initialization script
├── requirements.txt     # Python dependencies
└── api/                 # Additional API endpoints
```

## 🔧 API Endpoints

### Chat
- `POST /chat` - Send message to AI chatbot

### Doctors
- `GET /doctors/` - Get all doctors
- `GET /doctors/specialty/{specialty}` - Get doctors by specialty

### Appointments
- `GET /appointments/` - Get all appointments
- `POST /appointments/` - Book new appointment

### Debug
- `GET /debug/doctors` - Debug endpoint to check database

## 🗄️ Database

The application uses SQLite with the following models:
- **Doctor**: Doctor information and specialties
- **Patient**: Patient details
- **Appointment**: Appointment bookings
- **DoctorAvailability**: Doctor availability schedules

## 🤖 AI Integration

The backend integrates with OpenAI GPT-3.5-turbo for:
- Natural language processing
- Function calling for structured responses
- Medical conversation handling

## 🔒 Environment Variables

- `OPENAI_API_KEY`: OpenAI API key for AI functionality
- `DATABASE_URL`: Database connection URL

## 📚 API Documentation

Visit `/docs` endpoint for interactive API documentation when running locally.

## 🚀 Deployment

The backend is configured for deployment on Render with:
- Automatic builds from GitHub
- Environment variable configuration
- Database initialization on startup
