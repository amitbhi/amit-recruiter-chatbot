# 🚀 Frontend-Backend Integration Guide

## Overview

This package contains:
1. **Updated Frontend** - Your beautiful HTML profile with RAG chatbot integration
2. **RAG Backend** - Python FastAPI backend (in the `recruiter-rag-bot` folder)

## 📦 What's Included

### Frontend Files (Use these!)
- `index.html` - Updated homepage with correct publication info
- `chat.html` - AI chat interface with API configuration
- `style.css` - Your existing styles (copy from your profile folder)
- `script.js` - Your existing animations (copy from your profile folder)
- `profile.jpg` - Your profile image (copy from your profile folder)

### Backend (Already provided earlier)
- See the `recruiter-rag-bot` folder for complete backend

## 🎯 Step-by-Step Integration

### Option 1: Test Locally (Recommended First)

#### Step 1: Start the Backend

```bash
# Navigate to backend folder
cd recruiter-rag-bot

# Set your Groq API key
export GROQ_API_KEY="your_groq_api_key_here"

# Install dependencies (if not done already)
pip install -r requirements.txt

# Run the API
python app.py
```

The backend will start at `http://localhost:8000`

#### Step 2: Set Up Frontend

1. **Copy these files to your existing profile folder:**
   - Replace your `index.html` with the new one
   - Replace your `chat.html` with the new one
   - Keep your existing `style.css`, `script.js`, `profile.jpg`

2. **Open chat.html in your browser:**
   - Open `file:///path/to/your/profile/chat.html`
   - Or use a simple local server:
     ```bash
     python -m http.server 8080
     # Visit http://localhost:8080/chat.html
     ```

3. **Configure the API:**
   - Click the gear icon (⚙️) in the chat interface
   - API URL should be: `http://localhost:8000`
   - Click "Test & Save"
   - Should show "✅ Connected!"

4. **Start Chatting!**
   - Ask questions like:
     - "What is Amit's experience with AI?"
     - "Tell me about Suzlon achievements"
     - "Has Amit published research?"

### Option 2: Deploy to Production (Free)

#### Backend Deployment (Render.com)

Follow the `DEPLOYMENT.md` in the `recruiter-rag-bot` folder to deploy your backend to Render.com (free).

Once deployed, you'll get a URL like: `https://amit-recruiter-chatbot.onrender.com`

#### Frontend Deployment

You can host your frontend on:
- **GitHub Pages** (free)
- **Netlify** (free)
- **Vercel** (free)

**Example: GitHub Pages**

1. Create a new GitHub repository for your profile
2. Push all frontend files (index.html, about.html, chat.html, style.css, script.js, images)
3. Enable GitHub Pages in repository settings
4. Your site will be live at: `https://yourusername.github.io/your-repo-name`

#### Connect Frontend to Deployed Backend

1. Once your frontend is live, open `chat.html`
2. Click the gear icon (⚙️)
3. Change API URL to your Render URL: `https://amit-recruiter-chatbot.onrender.com`
4. Click "Test & Save"
5. Done! ✅

## 🔧 Configuration

### Changing API URL (Future Updates)

The chat interface has a built-in settings panel:

1. Click the **gear icon (⚙️)** in the chat header
2. Update the API URL
3. Click "Test & Save" to verify connection
4. Settings are saved in browser localStorage

### Changing Groq API Key

For the backend:

**Local:**
```bash
export GROQ_API_KEY="new_key_here"
python app.py
```

**Render.com:**
1. Go to your Render dashboard
2. Select your web service
3. Go to "Environment"
4. Update `GROQ_API_KEY` value
5. Service will auto-redeploy

### Updating Knowledge Base

To update Amit's profile information:

1. Edit `knowledge_base.txt` in the backend folder
2. For local: Restart the backend (it will rebuild the vector database)
3. For Render: Push changes to GitHub, Render will auto-deploy

## 📋 File Checklist

Before deploying, make sure you have:

**Frontend:**
- ✅ index.html (updated with correct publications)
- ✅ about.html (your existing one is fine, or update from documents)
- ✅ chat.html (new one with API integration)
- ✅ style.css (your existing one)
- ✅ script.js (your existing one)
- ✅ profile.jpg (your profile image)
- ✅ documents/ folder (with your LOR PDFs)

**Backend:**
- ✅ All files from `recruiter-rag-bot` folder
- ✅ Groq API key configured
- ✅ Deployed to Render.com (or running locally)

## 🐛 Troubleshooting

### "Could not connect to API"

**Problem:** Frontend can't reach backend

**Solutions:**
1. Make sure backend is running (`python app.py`)
2. Check API URL in settings (gear icon)
3. For local testing: Use `http://localhost:8000` (not https)
4. For production: Use your Render URL

### "API returned 500"

**Problem:** Backend error

**Solutions:**
1. Check backend logs
2. Verify Groq API key is set correctly
3. Make sure knowledge_base.txt exists

### "Typing... never stops"

**Problem:** API request hanging

**Solutions:**
1. Check your network connection
2. For Render free tier: First request after inactivity takes 30-60 seconds
3. Refresh the page and try again

### CORS Errors

**Problem:** Browser blocking requests

**Solution:** The backend already has CORS enabled. If you still see errors:
- Make sure you're using the same protocol (http/http or https/https)
- For production, both frontend and backend should use https

## 🎨 Customization

### Change Chatbot Personality

Edit `rag_engine.py` line ~95:
```python
system_prompt = """You are a helpful AI assistant...
```

### Add More Sample Questions

Edit `chat.html` line ~580:
```html
💡 Try: "Your question" • "Another question" • "More questions"
```

### Change Colors/Theme

Edit `style.css` - the CSS variables at the top:
```css
:root {
    --accent: #2dd4bf;  /* Change this for different accent color */
    ...
}
```

## 📊 Updated Publications

Your profile now shows:

1. **Engineering Applications of Artificial Intelligence**
   - Title: Personal Logs as First-Class Longitudinal Data Objects...
   - DOI: https://doi.org/10.2139/ssrn.6579749

2. **International Journal of Human-Computer Studies**
   - Title: Multi-Agent Graph-Based Intelligent Decision Support System...
   - Status: Under Review

3. **Applied Research Paper**
   - Title: Knowledge Graph-Driven Operational Intelligence...
   - Status: To be published

## 💡 Tips

1. **Test locally first** before deploying to production
2. **Free tier limits:** Render spins down after 15 min inactivity (first request is slow)
3. **Save API settings:** The chat interface remembers your API URL in localStorage
4. **Mobile friendly:** Everything works on mobile too!

## 🆘 Need Help?

If something isn't working:
1. Check browser console for errors (F12)
2. Check backend logs if running locally
3. Make sure all files are in the right place
4. Verify API key is set correctly

## 🎉 You're All Set!

Once everything is configured:
1. Share your frontend URL with recruiters
2. They can chat with your AI profile
3. All responses come from your actual profile data
4. 100% free hosting!

---

**Questions?** The chat interface is now fully functional and ready to showcase your profile to recruiters!
