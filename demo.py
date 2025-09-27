#!/usr/bin/env python3
"""
Demo script for Doctor's Assistant Chatbot
"""
import requests
import json
import time

BASE_URL = "http://localhost:8000"

def print_chat(message, is_user=True):
    """Print chat message with formatting"""
    prefix = "👤 You" if is_user else "🤖 Bot"
    print(f"{prefix}: {message}")
    print("-" * 50)

def demo_conversation():
    """Demonstrate the chatbot capabilities"""
    print("🏥 Doctor's Assistant Chatbot Demo")
    print("=" * 50)
    print("This demo shows the three main conversation scenarios from the requirements.")
    print()
    
    session_id = None
    
    # Scenario 1: Direct appointment booking
    print("📅 SCENARIO 1: Direct Appointment Booking")
    print("=" * 50)
    
    messages = [
        "Hi can I have an appointment with Dr. Sarah Johnson",
        "I would like to meet her tomorrow at 10 AM",
        "Ok, that works for me"
    ]
    
    for message in messages:
        print_chat(message, is_user=True)
        
        response = requests.post(f"{BASE_URL}/chat", json={
            "message": message,
            "session_id": session_id
        })
        
        if response.status_code == 200:
            result = response.json()
            session_id = result['session_id']
            print_chat(result['response'], is_user=False)
            
            if result.get('function_called'):
                print(f"🔧 Function called: {result['function_called']}")
        else:
            print(f"❌ Error: {response.status_code}")
        
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print("📅 SCENARIO 2: Symptom-Based Consultation")
    print("=" * 50)
    
    # Reset session for new scenario
    session_id = None
    
    messages = [
        "Hi, I have been having these rashes for the past few days. Would like to meet a doctor, could you help",
        "No, that's all I need"
    ]
    
    for message in messages:
        print_chat(message, is_user=True)
        
        response = requests.post(f"{BASE_URL}/chat", json={
            "message": message,
            "session_id": session_id
        })
        
        if response.status_code == 200:
            result = response.json()
            session_id = result['session_id']
            print_chat(result['response'], is_user=False)
            
            if result.get('function_called'):
                print(f"🔧 Function called: {result['function_called']}")
        else:
            print(f"❌ Error: {response.status_code}")
        
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print("📅 SCENARIO 3: Injury Consultation")
    print("=" * 50)
    
    # Reset session for new scenario
    session_id = None
    
    messages = [
        "Hi, I fell down while playing badminton - my ankle is swollen. Would like to meet a doctor today, could you help",
        "I would like to meet Dr. Michael Chen",
        "Oh! in that case can I meet Dr. Robert Wilson today",
        "Ok, that works"
    ]
    
    for message in messages:
        print_chat(message, is_user=True)
        
        response = requests.post(f"{BASE_URL}/chat", json={
            "message": message,
            "session_id": session_id
        })
        
        if response.status_code == 200:
            result = response.json()
            session_id = result['session_id']
            print_chat(result['response'], is_user=False)
            
            if result.get('function_called'):
                print(f"🔧 Function called: {result['function_called']}")
        else:
            print(f"❌ Error: {response.status_code}")
        
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print("✅ Demo completed!")
    print("=" * 50)

def check_server():
    """Check if the server is running"""
    try:
        response = requests.get(f"{BASE_URL}/")
        return response.status_code == 200
    except:
        return False

def main():
    """Main function"""
    print("Checking if server is running...")
    
    if not check_server():
        print("❌ Server is not running!")
        print("Please start the server first by running:")
        print("  python run.py")
        print("  or")
        print("  python main.py")
        return
    
    print("✅ Server is running!")
    print()
    
    try:
        demo_conversation()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during demo: {e}")

if __name__ == "__main__":
    main()
