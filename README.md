# Doctor's Assistant Chatbot

A FastAPI-based chatbot that helps patients book appointments with doctors using OpenAI's Completion API and Function Calling.

## Features

- **Natural Language Processing**: Chat with the bot using natural language
- **Function Calling**: The bot can check doctor availability, find specialists, and book appointments
- **Database Integration**: SQLite database to store doctors, patients, and appointments
- **RESTful API**: Complete API endpoints for managing doctors, patients, and appointments

## Requirements

- Python 3.8+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd doctor_chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file with your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///./doctors_clinic.db
```

4. Initialize the database with sample data:
```bash
python init_db.py
```

## Running the Application

1. Start the FastAPI server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. The API will be available at `http://localhost:8000`

3. View the interactive API documentation at `http://localhost:8000/docs`

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

## License

This project is licensed under the MIT License.
