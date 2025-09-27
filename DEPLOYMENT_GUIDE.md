# 🚀 Deployment Guide - Doctor's Assistant Chatbot

## 📋 Overview

This guide will help you deploy your Doctor's Assistant Chatbot to production:

- **Frontend (React)** → Vercel
- **Backend (FastAPI)** → Railway/Render/Heroku

## 🎯 Step 1: Deploy Backend (FastAPI)

### Option A: Railway (Recommended)

1. **Go to [Railway.app](https://railway.app)**
2. **Sign up/Login** with GitHub
3. **Click "New Project"** → **"Deploy from GitHub repo"**
4. **Select your repository:** `saggarz/doctor-chatbot`
5. **Configure the deployment:**
   - **Root Directory:** `/` (root of repository)
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`

6. **Add Environment Variables:**
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   DATABASE_URL=sqlite:///./doctors_clinic.db
   ```

7. **Deploy!** Railway will automatically build and deploy

### Option B: Render

1. **Go to [Render.com](https://render.com)**
2. **Sign up/Login** with GitHub
3. **Click "New"** → **"Web Service"**
4. **Connect your repository**
5. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`
   - **Python Version:** 3.11

6. **Add Environment Variables:**
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   DATABASE_URL=sqlite:///./doctors_clinic.db
   ```

### Option C: Heroku

1. **Install Heroku CLI**
2. **Login:** `heroku login`
3. **Create app:** `heroku create your-app-name`
4. **Add buildpack:** `heroku buildpacks:set heroku/python`
5. **Set environment variables:**
   ```bash
   heroku config:set OPENAI_API_KEY=your_openai_api_key_here
   heroku config:set DATABASE_URL=sqlite:///./doctors_clinic.db
   ```
6. **Deploy:** `git push heroku main`

## 🎨 Step 2: Deploy Frontend (React) to Vercel

### Method 1: Vercel CLI (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Navigate to frontend:**
   ```bash
   cd frontend
   ```

3. **Login to Vercel:**
   ```bash
   vercel login
   ```

4. **Deploy:**
   ```bash
   vercel
   ```

5. **Follow the prompts:**
   - **Set up and deploy?** Yes
   - **Which scope?** Your account
   - **Link to existing project?** No
   - **Project name:** doctor-chatbot-frontend
   - **Directory:** `./frontend`
   - **Override settings?** No

### Method 2: Vercel Dashboard

1. **Go to [Vercel.com](https://vercel.com)**
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Import your repository:** `saggarz/doctor-chatbot`
5. **Configure:**
   - **Root Directory:** `frontend`
   - **Framework Preset:** Vite
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`

6. **Add Environment Variables:**
   ```
   VITE_API_URL=https://your-backend-url.railway.app
   ```

7. **Deploy!**

## 🔧 Step 3: Configure Environment Variables

### Backend Environment Variables:
```
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///./doctors_clinic.db
```

### Frontend Environment Variables:
```
VITE_API_URL=https://your-backend-url.railway.app
```

## 📱 Step 4: Update API Configuration

After deploying your backend, update the frontend API configuration:

1. **Get your backend URL** from Railway/Render/Heroku
2. **Update `frontend/src/services/api.ts`:**
   ```typescript
   const API_BASE_URL = import.meta.env.VITE_API_URL || '/api'
   ```

3. **Redeploy frontend** with the new environment variable

## 🎯 Step 5: Test Your Deployment

### Backend Testing:
```bash
# Test your backend API
curl https://your-backend-url.railway.app/
curl https://your-backend-url.railway.app/docs
```

### Frontend Testing:
1. **Visit your Vercel URL**
2. **Test all features:**
   - Dashboard loads
   - Chat interface works
   - Doctor list loads
   - Appointment booking works

## 🔄 Step 6: Continuous Deployment

### Automatic Deployments:
- **Push to main branch** → Automatic deployment
- **Railway/Render/Heroku** → Auto-deploys backend
- **Vercel** → Auto-deploys frontend

### Manual Deployments:
```bash
# Backend
git push origin main

# Frontend
cd frontend
vercel --prod
```

## 📊 Expected URLs

After deployment, you'll have:

- **Frontend:** `https://doctor-chatbot-frontend.vercel.app`
- **Backend:** `https://your-app-name.railway.app`
- **API Docs:** `https://your-app-name.railway.app/docs`

## 🛠️ Troubleshooting

### Common Issues:

1. **CORS Errors:**
   - Add your frontend URL to CORS origins in `main.py`

2. **Environment Variables:**
   - Make sure all env vars are set correctly
   - Check case sensitivity

3. **Build Failures:**
   - Check Python/Node versions
   - Verify all dependencies are in requirements.txt

4. **API Connection:**
   - Verify backend URL is correct
   - Check if backend is running

## 🎉 Success!

Once deployed, your Doctor's Assistant Chatbot will be live and accessible to users worldwide!

### Features Available:
- ✅ **AI-powered chat** with OpenAI
- ✅ **Doctor management** and search
- ✅ **Appointment booking** system
- ✅ **Responsive design** for all devices
- ✅ **Real-time conversations** with medical context

---

**Your medical AI assistant is now live on the internet!** 🌟
