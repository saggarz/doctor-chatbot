import openai
import json
from typing import Dict, List, Any, Optional
from config import OPENAI_API_KEY
from datetime import datetime, timedelta

openai.api_key = OPENAI_API_KEY

class OpenAIService:
    def __init__(self):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
        self.functions = self._define_functions()
        
    def _define_functions(self) -> List[Dict]:
        """Define the functions available for the chatbot"""
        return [
            {
                "name": "check_doctor_availability",
                "description": "Check if a specific doctor is available on a given date and time",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "doctor_name": {
                            "type": "string",
                            "description": "Name of the doctor to check availability for"
                        },
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format"
                        },
                        "time": {
                            "type": "string",
                            "description": "Time in HH:MM format"
                        }
                    },
                    "required": ["doctor_name", "date", "time"]
                }
            },
            {
                "name": "find_doctors_by_specialty",
                "description": "Find doctors by their medical specialty",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "specialty": {
                            "type": "string",
                            "description": "Medical specialty (e.g., dermatology, orthopedics, cardiology)"
                        }
                    },
                    "required": ["specialty"]
                }
            },
            {
                "name": "book_appointment",
                "description": "Book an appointment with a doctor",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "doctor_name": {
                            "type": "string",
                            "description": "Name of the doctor"
                        },
                        "patient_name": {
                            "type": "string",
                            "description": "Name of the patient"
                        },
                        "patient_phone": {
                            "type": "string",
                            "description": "Phone number of the patient"
                        },
                        "appointment_date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format"
                        },
                        "appointment_time": {
                            "type": "string",
                            "description": "Time in HH:MM format"
                        },
                        "notes": {
                            "type": "string",
                            "description": "Additional notes about the appointment"
                        }
                    },
                    "required": ["doctor_name", "patient_name", "appointment_date", "appointment_time"]
                }
            },
            {
                "name": "get_available_doctors",
                "description": "Get list of all available doctors for a specific date and time",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format"
                        },
                        "time": {
                            "type": "string",
                            "description": "Time in HH:MM format"
                        }
                    },
                    "required": ["date", "time"]
                }
            }
        ]
    
    def get_chat_completion(self, messages: List[Dict], functions: Optional[List[Dict]] = None) -> Dict:
        """Get chat completion from OpenAI with retry logic"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    functions=functions or self.functions,
                    function_call="auto",
                    temperature=0.7,
                    timeout=30  # Add timeout
                )
                
                return {
                    "success": True,
                    "response": response.choices[0].message,
                    "usage": response.usage
                }
            except Exception as e:
                if attempt == max_retries - 1:  # Last attempt
                    return {
                        "success": False,
                        "error": f"OpenAI API error after {max_retries} attempts: {str(e)}"
                    }
                # Wait before retry
                import time
                time.sleep(1 * (attempt + 1))  # Exponential backoff
    
    def get_simple_completion(self, messages: List[Dict]) -> Dict:
        """Get simple completion without function calling with retry logic"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=0.7,
                    timeout=30  # Add timeout
                )
                
                return {
                    "success": True,
                    "response": response.choices[0].message.content,
                    "usage": response.usage
                }
            except Exception as e:
                if attempt == max_retries - 1:  # Last attempt
                    return {
                        "success": False,
                        "error": f"OpenAI API error after {max_retries} attempts: {str(e)}"
                    }
                # Wait before retry
                import time
                time.sleep(1 * (attempt + 1))  # Exponential backoff
