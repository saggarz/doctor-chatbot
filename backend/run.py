#!/usr/bin/env python3
"""
Startup script for Doctor's Assistant Chatbot
"""
import os
import sys
from pathlib import Path

def check_requirements():
    """Check if all requirements are met"""
    print("Checking requirements...")
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("⚠️  .env file not found. Creating from template...")
        with open('.env', 'w') as f:
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
            f.write("DATABASE_URL=sqlite:///./doctors_clinic.db\n")
        print("✅ Created .env file. Please add your OpenAI API key.")
        return False
    
    # Check if OpenAI API key is set
    from dotenv import load_dotenv
    load_dotenv()
    
    if os.getenv("OPENAI_API_KEY") == "your_openai_api_key_here":
        print("⚠️  Please set your OpenAI API key in the .env file")
        return False
    
    print("✅ Requirements check passed")
    return True

def initialize_database():
    """Initialize the database with sample data"""
    print("Initializing database...")
    try:
        from init_db import init_database
        init_database()
        print("✅ Database initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        return False

def start_server():
    """Start the FastAPI server"""
    print("Starting FastAPI server...")
    try:
        import uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def main():
    """Main function"""
    print("🏥 Doctor's Assistant Chatbot")
    print("=" * 40)
    
    # Check requirements
    if not check_requirements():
        print("\nPlease fix the issues above and run again.")
        sys.exit(1)
    
    # Initialize database
    if not initialize_database():
        print("\nFailed to initialize database.")
        sys.exit(1)
    
    print("\n🚀 Starting server...")
    print("📖 API Documentation: http://localhost:8000/docs")
    print("💬 Chat endpoint: http://localhost:8000/chat")
    print("\nPress Ctrl+C to stop the server")
    
    # Start server
    start_server()

if __name__ == "__main__":
    main()
