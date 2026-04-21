# 🚀 Quick Deployment Guide

## Step-by-Step Deployment (5 minutes)

### 1️⃣ Get Your Groq API Key (2 minutes)

1. Go to: https://console.groq.com
2. Click "Sign Up" (use Google/GitHub for quick signup)
3. Go to "API Keys" section
4. Click "Create API Key"
5. Copy the key (it starts with `gsk_...`)
6. **Save it somewhere safe!**

### 2️⃣ Create GitHub Repository (1 minute)

1. Go to: https://github.com/new
2. Repository name: `amit-recruiter-chatbot`
3. Make it **Public** ✅ (required for free Render deployment)
4. Don't initialize with README
5. Click "Create repository"

### 3️⃣ Push Code to GitHub (1 minute)

Open terminal and run these commands:

```bash
cd /home/claude/recruiter-rag-bot

git init
git add .
git commit -m "Initial commit: RAG chatbot for Amit Bhise"
git branch -M main

# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/amit-recruiter-chatbot.git
git push -u origin main
```

**If git asks for credentials:**
- Username: Your GitHub username
- Password: Use a Personal Access Token (not your password)
  - Get token at: https://github.com/settings/tokens

### 4️⃣ Deploy on Render.com (2 minutes)

1. Go to: https://dashboard.render.com
2. Click "Sign Up" → Sign up with GitHub (easiest)
3. Click "New +" → "Web Service"
4. Click "Connect" next to your `amit-recruiter-chatbot` repository
5. Fill in the form:
   - **Name**: `amit-recruiter-chatbot`
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: `Free` ✅
6. Click "Advanced" → "Add Environment Variable"
   - **Key**: `GROQ_API_KEY`
   - **Value**: Paste your Groq API key (from step 1)
7. Click "Create Web Service"

### 5️⃣ Wait for Deployment (5-10 minutes)

- Render will build and deploy your app
- You'll see logs showing progress
- When you see "Application startup complete", it's ready!
- Copy your URL: `https://amit-recruiter-chatbot.onrender.com`

### 6️⃣ Test Your API

Visit these URLs (replace with your actual URL):

1. **Main page**: https://amit-recruiter-chatbot.onrender.com/
2. **Health check**: https://amit-recruiter-chatbot.onrender.com/health
3. **API docs**: https://amit-recruiter-chatbot.onrender.com/docs
4. **Try a query**: Go to `/docs`, expand POST `/query`, click "Try it out"

## 🎉 You're Done!

Your API is now live and free forever!

### Update Your Frontend

In your HTML frontend, change the API URL to:
```javascript
const API_URL = 'https://amit-recruiter-chatbot.onrender.com';
```

### Share with Recruiters

Give recruiters this link to your frontend, and it will query your deployed API!

## 🔧 Troubleshooting

**"API not responding"?**
- Wait 30-60 seconds - free tier spins down after inactivity
- First request wakes it up

**"Build failed"?**
- Check the logs in Render dashboard
- Make sure GROQ_API_KEY is set correctly

**"CORS error"?**
- The API already has CORS enabled for all origins
- Should work with any frontend

## 📱 Need Help?

Email: amitvishnu@gmail.com

---

**Next Steps:**
1. ✅ Test the API at `/docs`
2. ✅ Update your HTML frontend with the new API URL
3. ✅ Share your frontend URL with recruiters
4. ✅ Monitor usage in Render dashboard

**Total Cost: ₹0 / $0 / €0** 🎉
