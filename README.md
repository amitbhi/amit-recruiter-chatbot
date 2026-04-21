# Amit Bhise - Recruiter Chatbot (RAG Backend)

A **free** RAG-powered chatbot API that answers questions about Amit Bhise's professional profile. Built for recruiters and hiring managers.

## 🚀 Features

- **RAG (Retrieval-Augmented Generation)**: Answers based on comprehensive knowledge base
- **Free Stack**: 100% free infrastructure (Groq API + Render.com)
- **Fast Responses**: Using Groq's optimized LLM inference
- **REST API**: Easy integration with any frontend
- **CORS Enabled**: Works with HTML/JS frontends

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Vector Database**: ChromaDB (embedded, no separate DB needed)
- **Embeddings**: HuggingFace sentence-transformers (runs locally)
- **LLM**: Groq API (llama-3.1-8b-instant) - completely free
- **Deployment**: Render.com (free tier)

## 📋 Prerequisites

1. **Groq API Key** (free):
   - Go to https://console.groq.com
   - Sign up (no credit card required)
   - Create an API key
   - Copy the key

2. **GitHub Account** (free)

3. **Render Account** (free):
   - Go to https://render.com
   - Sign up with GitHub

## 🚀 Deployment Steps

### Step 1: Push to GitHub

1. **Create a new GitHub repository**:
   - Go to https://github.com/new
   - Name: `amit-recruiter-chatbot`
   - Make it **Public** (required for Render free tier)
   - Don't initialize with README (we already have one)

2. **Push this code to GitHub**:
   ```bash
   cd /home/claude/recruiter-rag-bot
   git init
   git add .
   git commit -m "Initial commit: RAG chatbot for Amit Bhise profile"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/amit-recruiter-chatbot.git
   git push -u origin main
   ```

### Step 2: Deploy on Render.com

1. **Go to Render Dashboard**: https://dashboard.render.com

2. **Click "New +" → "Web Service"**

3. **Connect GitHub repository**:
   - Select `amit-recruiter-chatbot`
   - Click "Connect"

4. **Configure the service**:
   - **Name**: `amit-recruiter-chatbot` (or any name you prefer)
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Select **Free**

5. **Add Environment Variable**:
   - Click "Add Environment Variable"
   - **Key**: `GROQ_API_KEY`
   - **Value**: Paste your Groq API key
   - Click "Save"

6. **Click "Create Web Service"**

7. **Wait for deployment** (5-10 minutes for first deployment)

8. **Get your API URL**:
   - Once deployed, you'll get a URL like: `https://amit-recruiter-chatbot.onrender.com`
   - This is your API endpoint!

### Step 3: Test Your API

Visit these URLs to test:

1. **API Root**: `https://your-app.onrender.com/`
2. **Health Check**: `https://your-app.onrender.com/health`
3. **API Docs**: `https://your-app.onrender.com/docs` (Swagger UI)
4. **Sample Questions**: `https://your-app.onrender.com/sample-questions`

## 📡 API Endpoints

### POST `/query`

Submit a question about Amit Bhise.

**Request**:
```json
{
  "question": "What is Amit's experience with AI?"
}
```

**Response**:
```json
{
  "question": "What is Amit's experience with AI?",
  "answer": "Amit has approximately 7+ years of experience with Generative AI and 11+ years in Data Science...",
  "sources": 5
}
```

### GET `/health`

Check if the API is running.

**Response**:
```json
{
  "status": "healthy",
  "rag_engine": "initialized",
  "vector_db_chunks": 45
}
```

### GET `/sample-questions`

Get example questions recruiters can ask.

## 🌐 Frontend Integration

### For HTML/JavaScript Frontend

```javascript
// Query the chatbot
async function askQuestion(question) {
    const response = await fetch('https://your-app.onrender.com/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: question })
    });
    
    const data = await response.json();
    return data.answer;
}

// Usage
const answer = await askQuestion("What is Amit's experience with AI?");
console.log(answer);
```

### Example HTML Implementation

```html
<!DOCTYPE html>
<html>
<head>
    <title>Chat with Amit's Profile</title>
</head>
<body>
    <div id="chat">
        <input type="text" id="question" placeholder="Ask about Amit...">
        <button onclick="ask()">Ask</button>
        <div id="response"></div>
    </div>

    <script>
        async function ask() {
            const question = document.getElementById('question').value;
            const response = await fetch('https://your-app.onrender.com/query', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question })
            });
            const data = await response.json();
            document.getElementById('response').innerText = data.answer;
        }
    </script>
</body>
</html>
```

## 🧪 Local Testing

Before deploying, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Set your Groq API key
export GROQ_API_KEY="your_groq_api_key_here"

# Run the server
python app.py
```

Visit: http://localhost:8000/docs

## 💡 Sample Questions

Your frontend can use these as suggestions:

- "What is Amit's experience with AI and machine learning?"
- "Tell me about Amit's key achievements at Suzlon Energy"
- "What technical skills does Amit have?"
- "What is Amit's educational background?"
- "Has Amit published any research papers?"
- "What programming languages does Amit know?"
- "What is Amit's experience with MLOps?"
- "Tell me about Amit's leadership experience"
- "How can I contact Amit?"
- "Is Amit open to relocation?"

## 🔄 Updating the Knowledge Base

To update Amit's profile information:

1. Edit `knowledge_base.txt`
2. Commit and push to GitHub
3. Render will auto-deploy the changes
4. The vector database will rebuild on next startup

## 📊 Monitoring

**Render Free Tier Limits**:
- ⏱️ Spins down after 15 minutes of inactivity
- 🔄 First request after spin-down takes 30-60 seconds
- 📈 750 hours/month of runtime (plenty for a chatbot)
- 💾 No persistent disk (ChromaDB rebuilds on restart)

**Groq Free Tier**:
- 🚀 14,400 requests per day
- ⚡ 30 requests per minute
- 💰 100% free forever

## 🐛 Troubleshooting

**API returns error on first request after inactivity?**
- Normal! Free tier spins down. Second request will work.

**ChromaDB errors?**
- Delete `chroma_db/` folder and restart to rebuild vector database

**Groq API key error?**
- Check environment variable is set correctly on Render

**CORS errors from frontend?**
- API has CORS enabled for all origins (`allow_origins=["*"]`)
- For production, update this in `app.py` to your frontend domain

## 📞 Contact

For questions about this API or Amit Bhise's profile:
- Email: amitvishnu@gmail.com
- Phone: +91 98908 97285

## 📄 License

© 2025 Amit Bhise. All Rights Reserved.

---

**Built with ❤️ for recruiters worldwide**
