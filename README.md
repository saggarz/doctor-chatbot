# Doctor's Assistant Chatbot

An AI-powered medical assistant chatbot built with FastAPI, React, and OpenAI GPT-3.5-turbo.

## 🏗️ Project Structure

```
doctor-chatbot/
├── backend/          # FastAPI backend (deployed on Render)
│   ├── main.py      # FastAPI application
│   ├── models.py    # Database models
│   ├── services.py  # Business logic
│   └── ...
└── frontend/        # React frontend (deployed on Vercel)
    ├── src/         # React components
    ├── package.json # Frontend dependencies
    └── ...
```

## 🚀 Quick Start

### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend (React)
```bash
cd frontend
npm install
npm run dev
```

## 🌐 Live Demo

- **Frontend**: https://doctor-chatbot.vercel.app
- **Backend API**: https://doctor-chatbot-api-5v9h.onrender.com/docs

## 🛠️ Technology Stack

### Backend
- FastAPI (Python web framework)
- SQLAlchemy (ORM)
- SQLite (Database)
- OpenAI GPT-3.5-turbo (AI)
- Render (Hosting)

### Frontend
- React 18 (UI framework)
- TypeScript (Type safety)
- Tailwind CSS (Styling)
- Framer Motion (Animations)
- Vercel (Hosting)

## 📋 Features

- 🤖 AI-powered chat interface
- 👨‍⚕️ Doctor search and filtering
- 📅 Appointment booking
- 📱 Responsive design
- 🔒 Secure API endpoints

## 🔧 Development

### Backend Development
```bash
cd backend
python main.py
```

### Frontend Development
```bash
cd frontend
npm run dev
```

## 📚 Documentation

- [Backend API Documentation](https://doctor-chatbot-api-5v9h.onrender.com/docs)
- [Frontend Setup Guide](frontend/README.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details