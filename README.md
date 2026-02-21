# AI Agent Development Kit - Market Research Agent

A beginner-friendly Python project demonstrating **Google's Agent Development Kit (ADK)** with a real-world use case.

## 🤖 What This Project Does

This project builds an **AI Agent** that automatically:
1. **Researches companies** - Gathers information about target companies
2. **Analyzes markets** - Studies industry trends and competitor activities
3. **Generates reports** - Creates professional market analysis documents
4. **Sends insights** - Emails findings to stakeholders (optional)

Instead of you manually researching and writing reports, the AI agent does all this work for you!

## 📋 Project Structure

```
first-adk-project/
├── main.py                 # Entry point - run this to use the agent
├── config.py              # Configuration and setup
├── requirements.txt       # Python dependencies
├── .env.example           # Template for API keys (rename to .env)
├── .gitignore             # Keep secrets safe
├── README.md              # This file
├── agents/
│   └── market_researcher.py    # The main AI agent definition
└── tools/
    └── web_tools.py            # Tools the agent can use
```

## 🚀 Quick Start Guide

### Step 1: Set Up Your Workspace

```bash
# Navigate to project directory
cd /Users/swethasailesh/Documents/first-adk-project

# Create a virtual environment (isolated workspace)
python3 -m venv venv

# Activate it
source venv/bin/activate  # On macOS/Linux
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Get Your API Keys

You need "secret badges" for the AI brain to work:

1. **Google Gemini API Key** - Get from [Google AI Studio](https://aistudio.google.com)
   - Free tier available!
2. **Optional Anthropic Claude API Key** - Get from [Anthropic Console](https://console.anthropic.com)
3. **Optional Search API** - For web research capabilities

### Step 4: Configure Your Agent

```bash
# Copy the template
cp .env.example .env

# Edit .env and add your API keys
nano .env  # or use your favorite editor
```

The `.env` file looks like:
```
GOOGLE_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here (optional)
AGENT_MODEL=google  # or "anthropic"
```

### Step 5: Run Your Agent

```bash
# Start the agent
python main.py

# Or run as a web interface
python main.py --web
```

## 🧠 How the AI Agent Works

### 1. **The Agent's Brain** 
Powered by Google's Gemini AI (or Claude). The AI model that:
- Understands your requests
- Plans what steps to take
- Makes decisions about which tools to use

### 2. **The Agent's Tools**
Tools are like the agent's hands. Our agent can:
- `search_company_info` - Find information about a company
- `analyze_market_trends` - Research industry trends
- `search_news` - Get latest news and events
- `generate_report` - Create professional reports
- `send_email` - Email the findings (optional)

### 3. **The Agent's Workflow**
When you ask the agent to research Apple Inc:

```
You: "Research Apple Inc and generate a market report"
    ↓
[Agent's Brain] "I need to find: company info, market position, recent news"
    ↓
[Agent Uses Tools]
  - search_company_info("Apple") → Gets company details
  - analyze_market_trends("iPhone market", "AI sector")
  - search_news("Apple recent") → Gets latest developments
    ↓
[Agent Analyzes] "Here's what I found..."
    ↓
[Agent Uses Tools]
  - generate_report() → Creates structured analysis
  - send_email("report.pdf") → Shares with team
    ↓
You: Get a professional market research report!
```

## 📖 Understanding the Code

### `config.py`
Sets up the environment and API connections. Think of it as the hiring process:
- Checks if you have API keys
- Loads your preferences
- Initializes the AI model

### `tools/web_tools.py`
Defines what tools the agent can use. Like teaching an employee their job:
- Each tool is a function with clear description
- Agent reads the description and uses it when needed
- Tools can call real APIs or perform actions

### `agents/market_researcher.py`
This is the agent itself. The job description:
- Who is this agent (name, personality)
- Which tools it can use
- How to handle requests

### `main.py`
The command center:
- Gets your request
- Sends it to the agent
- Displays the agent's work

## 🎯 Real-World Use Cases

This pattern works for many scenarios:

1. **Business Intelligence** - Research competitors, market trends
2. **Content Creation** - Write blog posts, newsletters, reports
3. **Customer Support** - Answer questions, resolve issues
4. **Data Analysis** - Analyze datasets, generate insights
5. **Email Management** - Process emails, sort, respond
6. **Project Management** - Schedule tasks, track progress
7. **Research Assistant** - Literature review, data gathering

## 🔧 Testing Your Agent

The ADK includes a web interface to test:

```bash
# Start the testing interface
python main.py --web

# Opens http://localhost:8000
# You can chat with your agent and see its thinking process!
```

## 📚 The 4 Steps In This Project

Following the ADK guide:

1. ✅ **Setting Up Workspace** - Project structure, virtual environment
2. ✅ **Giving Permission** - API keys in `.env` file
3. ✅ **Teaching the Agent** - Tools defined in `tools/web_tools.py`
4. ✅ **Test & Launch** - Web interface for testing, deploy-ready code

## 🚀 Next Steps: Deploy to Cloud

Once satisfied with testing, deploy to:
- **Google Vertex AI** - Scalable, integrated with Google services
- **Cloud Run** - Fast, cost-effective
- **AWS Lambda** - If you prefer AWS ecosystem

Deployment makes your agent run 24/7 on the cloud!

## 🛡️ Security Best Practices

- **Never commit `.env` file** - It contains secrets!
- Use `.env.example` as a template
- Rotate API keys regularly
- Use IAM roles instead of API keys when possible
- Add `.gitignore` to prevent accidents

## ❓ Troubleshooting

### "Agent not responding"
- Check your API key is correct in `.env`
- Verify internet connection
- Check API quotas and rate limits

### "Tool not found"
- Ensure tool is defined in `tools/web_tools.py`
- Check tool name matches exactly
- Verify tool description is clear

### "Running out of API quota"
- Check your API usage in console
- Consider using free tier limits wisely
- Upgrade to paid plan if needed

## 📖 Learn More

- [Google ADK Documentation](https://ai.google.dev/adk)
- [Gemini API Guide](https://ai.google.dev/gemini-api)
- [Agent Design Patterns](https://cloud.google.com/vertex-ai/docs/agents)
- [Python Best Practices](https://peps.python.org/pep-0008/)

## 💡 Fun Exercises

1. **Add a new tool** - Create a `calculate_roi()` tool
2. **Chain agents** - Create a "Researcher" agent and a "Writer" agent
3. **Add memory** - Make the agent remember previous conversations
4. **Custom tools** - Connect to real APIs (Stripe, Gmail, Slack)
5. **Web deployment** - Deploy to Google Cloud

---

**Happy Agent Building! 🤖✨**

Remember: The future isn't about rigid software that just follows orders. It's about smart agents that understand your goals and make it happen.
