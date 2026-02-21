# 🚀 Quick Start Guide

Get your Market Research AI Agent up and running in 5 minutes!

## Step 1: Setup (2 minutes)

```bash
# Navigate to project
cd /Users/your_username/Documents/first-adk-project

# Create Python virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

## Step 2: Install Dependencies (1 minute)

```bash
pip install -r requirements.txt
```

## Step 3: Get Your API Key (1 minute)

1. Go to [Google AI Studio](https://aistudio.google.com)
2. Click "Get API Key"
3. Copy your key

## Step 4: Configure Agent (1 minute)

```bash
# Copy the template
cp .env.example .env

# Edit .env and paste your API key
# GOOGLE_API_KEY=paste_your_key_here
```

## Step 5: Run! 🎉

```bash
# Run demo
python main.py

# Or interactive mode
python main.py --interactive

# Or custom research
python main.py --research "Apple Inc market analysis"
```

## 🎯 Example Queries

Try these research requests:

- "Research Apple Inc and generate a market report"
- "Analyze the smartphone market trends"
- "Compare Apple and Microsoft as competitors"
- "Find the latest news about tech companies"
- "Generate a comprehensive market analysis report"

## 📊 What You'll See

The agent will:
1. ✅ Understand your research request
2. ✅ Plan what information to gather
3. ✅ Use tools to research companies and markets
4. ✅ Generate insights and reports
5. ✅ Present findings in a professional format

## 🛠️ Common Issues

### "API Key not found"
- Make sure you completed Step 3 and Step 4
- Check .env file has GOOGLE_API_KEY with correct value

### "Module not found"
- Make sure venv is activated
- Run: `pip install -r requirements.txt`

### "Connection error"
- Check internet connection
- Verify API key is valid (try at Google AI Studio)

## 💡 Next Steps

- Read the full [README.md](README.md)
- Check out [tools/web_tools.py](tools/web_tools.py) to see available tools
- Edit [agents/market_researcher.py](agents/market_researcher.py) to customize
- Add new tools for your specific needs

## 🎓 Learning Path

1. **Understand**: See what the agent is doing with `--info`
   ```bash
   python main.py --info
   ```

2. **Explore**: List available tools
   ```bash
   python main.py --tools
   ```

3. **Experiment**: Try different queries
   ```bash
   python main.py --research "your query"
   ```

4. **Customize**: Edit agent behavior in Python files

5. **Extend**: Add new tools and capabilities

## 📚 Key Files to Know

- `main.py` - Entry point, CLI interface
- `config.py` - Configuration and API setup
- `agents/market_researcher.py` - The agent definition
- `tools/web_tools.py` - Available tools for the agent
- `.env` - Your secret API keys (don't commit!)

## ✨ Fun Extensions

Once you're comfortable:

1. **Add Database Tool** - Store and retrieve research history
2. **Add Email Tool** - Send reports automatically
3. **Chain Agents** - Researcher + Writer + Publisher
4. **Web Dashboard** - Visualize research results
5. **Slack Integration** - Run agent from Slack commands

Happy researching! 🤖📊
