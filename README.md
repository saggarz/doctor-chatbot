# 🏥 Doctor's Assistant AI Chatbot

A complete, production-ready AI-powered medical assistant with a beautiful modern frontend and robust FastAPI backend.

## ✨ Features

### 🤖 AI-Powered Chat
- **Natural Language Processing** with OpenAI GPT-3.5-turbo
- **Function Calling** for intelligent responses
- **Real-time conversations** with medical context
- **Smart appointment booking** through chat

### 🎨 Beautiful Modern Frontend
- **React 18** with TypeScript for type safety
- **Tailwind CSS** for stunning, responsive design
- **Framer Motion** for smooth animations
- **Glass morphism effects** and gradient backgrounds
- **Mobile-first responsive** design

### 🏥 Medical Features
- **Doctor management** with search and filtering
- **Appointment booking** with step-by-step wizard
- **Specialty-based** doctor recommendations
- **Availability checking** and time slot selection
- **Patient information** collection and storage

### 🚀 Backend Architecture
- **FastAPI** for high-performance API
- **SQLAlchemy** for database management
- **OpenAI Integration** with retry logic
- **Error handling** and graceful degradation
- **RESTful API** with comprehensive endpoints

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** for backend
- **Node.js 18+** for frontend
- **OpenAI API key** for AI functionality

### 1. Clone Repository
```bash
git clone <repository-url>
cd doctor_chatbot
```

### 2. Backend Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Set up environment variables
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
echo "DATABASE_URL=sqlite:///./doctors_clinic.db" >> .env

# Initialize database
python init_db.py

# Start backend server
python main.py
```

### 3. Frontend Setup
```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### 4. Access Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## API Endpoints

### Chat Endpoint
- **POST** `/chat` - Main chatbot endpoint for natural language conversations

### Doctor Management
- **GET** `/doctors/` - Get all doctors
- **POST** `/doctors/` - Create a new doctor
- **GET** `/doctors/specialty/{specialty}` - Get doctors by specialty

### Patient Management
- **GET** `/patients/` - Get all patients
- **POST** `/patients/` - Create a new patient

### Appointment Management
- **GET** `/appointments/` - Get all appointments
- **POST** `/appointments/` - Create an appointment

### Doctor Availability
- **GET** `/doctor-availability/` - Get doctor availability
- **POST** `/doctor-availability/` - Set doctor availability

## Usage Examples

### 1. Chat with the Bot

```python
import requests

# Start a conversation
response = requests.post("http://localhost:8000/chat", json={
    "message": "Hi, I need to see a doctor for my knee pain"
})

print(response.json()["response"])
```

### 2. Book an Appointment

```python
# The bot will guide you through the booking process
response = requests.post("http://localhost:8000/chat", json={
    "message": "I want to book an appointment with Dr. Michael Chen for tomorrow at 2 PM",
    "session_id": "your-session-id"
})
```

### 3. Find Specialists

```python
# Ask for specialists
response = requests.post("http://localhost:8000/chat", json={
    "message": "I have skin problems, which doctor should I see?"
})
```

## Sample Conversations

The chatbot supports the following conversation patterns:

### Scenario 1: Direct Appointment Booking
```
User: "Hi can I have an appointment with Dr. Sarah Johnson"
Bot: "Sure, what date and time would you like the appointment?"
User: "I would like to meet him tomorrow at 10 AM"
Bot: "Sorry, he is not available at 10 AM, are you available at 11 AM?"
User: "Ok"
Bot: "Great, appointment is booked!"
```

### Scenario 2: Symptom-Based Consultation
```
User: "Hi, I have been having these rashes for the past few days. Would like to meet a doctor, could you help"
Bot: "You would have to see a dermatologist for this problem. We have Dr. Emily Davis available. Would you like to book an appointment?"
```

### Scenario 3: Injury Consultation
```
User: "Hi, I fell down while playing badminton - my ankle is swollen. Would like to meet a doctor today, could you help"
Bot: "Sure, which of the following orthopedic doctor(s) would you like to meet? Dr. Michael Chen, Dr. Robert Wilson"
```

## Testing

Run the test script to verify the API:

```bash
python test_api.py
```

## Database Schema

- **Doctors**: Store doctor information (name, specialty, department)
- **Patients**: Store patient information (name, phone, email)
- **Appointments**: Store appointment details (doctor, patient, date, time, status)
- **DoctorAvailability**: Store doctor's working hours and days

## Function Calling

The chatbot uses OpenAI's function calling feature to:

1. **check_doctor_availability**: Check if a doctor is available at a specific time
2. **find_doctors_by_specialty**: Find doctors by medical specialty
3. **book_appointment**: Book an appointment with a doctor
4. **get_available_doctors**: Get all available doctors for a specific time

## Configuration

The application can be configured through environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key
- `DATABASE_URL`: Database connection string (default: SQLite)

## Development

To add new features:

1. Add new functions to `openai_service.py`
2. Implement the corresponding logic in `services.py`
3. Update the API endpoints in `main.py`
4. Test with the chat interface

## 📁 Project Structure

```
doctor_chatbot/
├── 📁 frontend/                 # React frontend
│   ├── 📁 src/
│   │   ├── 📁 components/       # React components
│   │   │   ├── Header.tsx       # Navigation header
│   │   │   ├── Dashboard.tsx    # Home page
│   │   │   ├── ChatInterface.tsx # AI chat
│   │   │   ├── DoctorList.tsx   # Doctor listing
│   │   │   └── AppointmentBooking.tsx # Booking wizard
│   │   ├── 📁 services/         # API services
│   │   ├── 📁 types/            # TypeScript types
│   │   ├── App.tsx              # Main app
│   │   └── main.tsx             # Entry point
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.ts
├── 📄 main.py                   # FastAPI application
├── 📄 models.py                  # Database models
├── 📄 services.py                # Business logic
├── 📄 openai_service.py         # OpenAI integration
├── 📄 database.py               # Database config
├── 📄 init_db.py                # Database initialization
├── 📄 requirements.txt          # Python dependencies
├── 📄 run.py                    # Startup script
├── 📄 demo.py                   # Demo script
└── 📄 README.md                 # This file
```

## 🎯 Key Features

### 🤖 AI Chat Interface
- **Natural conversations** with medical context
- **Function calling** for intelligent responses
- **Real-time messaging** with typing indicators
- **Quick action buttons** for common requests

### 🏥 Medical Management
- **Doctor profiles** with specialties and availability
- **Appointment booking** with step-by-step wizard
- **Patient information** collection and storage
- **Search and filtering** capabilities

### 🎨 Modern UI/UX
- **Glass morphism** effects and gradients
- **Smooth animations** with Framer Motion
- **Responsive design** for all devices
- **Professional medical** theme

### 🚀 Performance
- **FastAPI** for high-performance backend
- **Vite** for lightning-fast frontend builds
- **TypeScript** for type safety
- **Optimized assets** and code splitting

## 🔧 Development

### Backend Development
```bash
# Start with auto-reload
python main.py

# Or with uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development
```bash
cd frontend
npm run dev
```

### Testing
```bash
# Test API endpoints
python test_api.py

# Run demo
python demo.py
```

## 📊 Database Schema

- **Doctors**: Name, specialty, department, availability
- **Patients**: Name, phone, email, created date
- **Appointments**: Doctor, patient, date, time, status
- **Doctor Availability**: Working hours and days

## 🌟 Highlights

✅ **Production-ready** codebase  
✅ **Beautiful modern UI** with animations  
✅ **AI-powered conversations** with OpenAI  
✅ **Complete appointment system**  
✅ **Responsive design** for all devices  
✅ **Type-safe** development  
✅ **Comprehensive documentation**  
✅ **Easy setup** and deployment  

## 📞 Support

For issues or questions:
- Check the console for errors
- Verify API endpoints are working
- Ensure all dependencies are installed
- Review the documentation

---

**Built with ❤️ using modern web technologies for the best user experience.**
