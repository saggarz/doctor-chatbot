import requests
import json

# Test the chatbot API
BASE_URL = "http://localhost:8000"

def test_chat():
    """Test the chat endpoint with different scenarios"""
    
    # Test cases based on the requirements
    test_cases = [
        {
            "name": "Appointment booking with specific doctor",
            "message": "Hi can I have an appointment with Dr. Sarah Johnson"
        },
        {
            "name": "Symptom-based consultation",
            "message": "Hi, I have been having these rashes for the past few days. Would like to meet a doctor, could you help"
        },
        {
            "name": "Injury consultation",
            "message": "Hi, I fell down while playing badminton - my ankle is swollen. Would like to meet a doctor today, could you help"
        }
    ]
    
    session_id = None
    
    for i, test_case in enumerate(test_cases):
        print(f"\n--- Test Case {i+1}: {test_case['name']} ---")
        
        payload = {
            "message": test_case["message"],
            "session_id": session_id
        }
        
        try:
            response = requests.post(f"{BASE_URL}/chat", json=payload)
            response.raise_for_status()
            
            result = response.json()
            print(f"Response: {result['response']}")
            
            if result.get('function_called'):
                print(f"Function called: {result['function_called']}")
                print(f"Function result: {result['function_result']}")
            
            session_id = result['session_id']
            
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def test_doctors_endpoint():
    """Test the doctors endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/doctors/")
        response.raise_for_status()
        
        doctors = response.json()
        print(f"\n--- Available Doctors ---")
        for doctor in doctors:
            print(f"Dr. {doctor['name']} - {doctor['specialty']} ({doctor['department']})")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Testing Doctor's Assistant Chatbot API")
    print("Make sure the server is running on http://localhost:8000")
    
    # Test doctors endpoint
    test_doctors_endpoint()
    
    # Test chat functionality
    test_chat()
