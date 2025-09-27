# 🚀 Complete Vercel Deployment Guide

## 📋 Overview

Deploy both your **React frontend** and **FastAPI backend** on Vercel as a full-stack application.

## 🎯 Step 1: Prepare Your Repository

Your repository is already configured for Vercel deployment with:
- ✅ **Root `vercel.json`** - Full-stack configuration
- ✅ **API directory** - Backend code in `/api`
- ✅ **Frontend directory** - React app in `/frontend`
- ✅ **Environment variables** - Configured for production

## 🚀 Step 2: Deploy to Vercel

### Method 1: Vercel CLI (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy from project root:**
   ```bash
   vercel
   ```

4. **Follow the prompts:**
   - **Set up and deploy?** Yes
   - **Which scope?** Your account
   - **Link to existing project?** No
   - **Project name:** doctor-chatbot
   - **Directory:** `./` (current directory)
   - **Override settings?** No

### Method 2: Vercel Dashboard

1. **Go to [Vercel.com](https://vercel.com)**
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Import your repository:** `saggarz/doctor-chatbot`
5. **Configure:**
   - **Framework Preset:** Other
   - **Root Directory:** `./` (root)
   - **Build Command:** (leave empty)
   - **Output Directory:** (leave empty)

## 🔧 Step 3: Configure Environment Variables

In Vercel Dashboard → Project Settings → Environment Variables:

### Required Variables:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Optional Variables:
```
DATABASE_URL=sqlite:///./doctors_clinic.db
```

## 📱 Step 4: Test Your Deployment

After deployment, you'll get URLs like:
- **Main App:** `https://doctor-chatbot.vercel.app`
- **API Endpoints:** `https://doctor-chatbot.vercel.app/api/`
- **API Docs:** `https://doctor-chatbot.vercel.app/api/docs`

### Test Endpoints:
```bash
# Test main app
curl https://doctor-chatbot.vercel.app/

# Test API
curl https://doctor-chatbot.vercel.app/api/

# Test chat endpoint
curl -X POST https://doctor-chatbot.vercel.app/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

## 🎯 Step 5: Verify Full-Stack Functionality

### Frontend Features:
- ✅ **Dashboard** loads with hero section
- ✅ **Chat interface** connects to API
- ✅ **Doctor list** loads from backend
- ✅ **Appointment booking** works
- ✅ **Responsive design** on all devices

### Backend Features:
- ✅ **API endpoints** respond correctly
- ✅ **OpenAI integration** works
- ✅ **Database operations** function
- ✅ **CORS** configured for frontend
- ✅ **Error handling** works properly

## 🔄 Step 6: Continuous Deployment

### Automatic Deployments:
- **Push to main branch** → Automatic deployment
- **Vercel** → Auto-deploys both frontend and backend
- **Environment variables** → Automatically applied

### Manual Deployments:
```bash
# Deploy latest changes
vercel --prod

# Deploy specific branch
vercel --prod --target production
```

## 📊 Project Structure on Vercel

```
doctor-chatbot.vercel.app/
├── /                    # React frontend (served as static files)
├── /api/                # FastAPI backend (Python serverless functions)
│   ├── /chat           # Chat endpoint
│   ├── /doctors/       # Doctor management
│   ├── /patients/      # Patient management
│   ├── /appointments/  # Appointment booking
│   └── /docs           # API documentation
```

## 🛠️ Troubleshooting

### Common Issues:

1. **Build Failures:**
   - Check Python version in `runtime.txt`
   - Verify all dependencies in `requirements.txt`
   - Check environment variables are set

2. **API Connection Issues:**
   - Verify `VITE_API_URL` is set to `/api`
   - Check CORS configuration in `main.py`
   - Test API endpoints directly

3. **Frontend Not Loading:**
   - Check build output in Vercel dashboard
   - Verify `frontend/vercel.json` configuration
   - Check for TypeScript errors

4. **Database Issues:**
   - SQLite files are ephemeral on Vercel
   - Consider using external database for production
   - Check database initialization in startup event

### Debug Commands:
```bash
# Check deployment logs
vercel logs

# Check function logs
vercel logs --follow

# Test locally
vercel dev
```

## 🎉 Success!

Once deployed, your Doctor's Assistant Chatbot will be live at:
- **URL:** `https://doctor-chatbot.vercel.app`
- **Features:** Full-stack AI-powered medical assistant
- **Performance:** Global CDN with edge functions
- **Scalability:** Automatic scaling with Vercel

### Features Available:
- ✅ **AI-powered chat** with OpenAI
- ✅ **Doctor management** and search
- ✅ **Appointment booking** system
- ✅ **Responsive design** for all devices
- ✅ **Real-time conversations** with medical context
- ✅ **Global deployment** with edge functions

---

**Your complete Doctor's Assistant is now live on Vercel!** 🌟
