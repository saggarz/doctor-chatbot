#!/usr/bin/env python3
"""
Setup script for Doctor's Assistant Chatbot
"""
import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def install_requirements():
    """Install required packages"""
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found")
        return False
    
    return run_command("pip install -r requirements.txt", "Installing requirements")

def create_env_file():
    """Create .env file if it doesn't exist"""
    if os.path.exists(".env"):
        print("✅ .env file already exists")
        return True
    
    print("📝 Creating .env file...")
    try:
        with open(".env", "w") as f:
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
            f.write("DATABASE_URL=sqlite:///./doctors_clinic.db\n")
        print("✅ .env file created")
        print("⚠️  Please edit .env file and add your OpenAI API key")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def initialize_database():
    """Initialize the database"""
    return run_command("python init_db.py", "Initializing database")

def main():
    """Main setup function"""
    print("🏥 Doctor's Assistant Chatbot Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print("❌ Failed to install requirements")
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        print("❌ Failed to create .env file")
        sys.exit(1)
    
    # Initialize database
    if not initialize_database():
        print("❌ Failed to initialize database")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env file and add your OpenAI API key")
    print("2. Run the application: python run.py")
    print("3. Or start manually: python main.py")
    print("4. Visit http://localhost:8000/docs for API documentation")

if __name__ == "__main__":
    main()
