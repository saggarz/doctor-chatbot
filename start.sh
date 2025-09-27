#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Start the application
python main.py
