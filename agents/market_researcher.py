"""
Market Research AI Agent

This is the core agent that uses Google's ADK to:
1. Understand research requests
2. Plan research steps using available tools
3. Execute research tools to gather data
4. Synthesize findings into insights
5. Generate reports
"""

import logging
from typing import Optional, List, Dict, Any
from datetime import datetime
import json

try:
    import google.generativeai as genai
except ImportError:
    genai = None

from config import get_model_config, AgentConfig, logger
from tools.web_tools import AVAILABLE_TOOLS, ResearchTools

logger = logging.getLogger(__name__)


class MarketResearchAgent:
    """
    AI Agent for market research and business intelligence.
    
    This agent can:
    - Research companies and industries
    - Analyze market trends
    - Compare competitors
    - Generate reports
    - Send findings via email
    """
    
    def __init__(self):
        """Initialize the market research agent."""
        self.name = AgentConfig.AGENT_NAME
        self.description = AgentConfig.AGENT_DESCRIPTION
        self.max_iterations = AgentConfig.MAX_ITERATIONS
        self.conversation_history = []
        self.research_results = {}
        
        # Initialize AI model
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize the AI model (Google Gemini)."""
        try:
            model_config = get_model_config()
            
            if model_config["type"] == "google":
                if genai is None:
                    raise ImportError("google-genai library not installed")
                
                genai.configure(api_key=model_config["api_key"])
                self.model = genai.GenerativeModel(model_config["model"])
                logger.info(f"✅ Initialized Google Gemini model")
            else:
                raise ValueError(f"Model type not supported in demo: {model_config['type']}")
        
        except Exception as e:
            logger.error(f"❌ Failed to initialize model: {e}")
            raise
    
    def research(self, query: str) -> str:
        """
        Execute research based on user query.
        
        The agent will:
        1. Understand what information is needed
        2. Plan research steps
        3. Use tools to gather data
        4. Synthesize findings
        
        Args:
            query: Research request (e.g., "Research Apple Inc and generate a market report")
        
        Returns:
            Research results as a formatted string
        """
        logger.info(f"🔬 Starting research: {query}")
        
        try:
            # Step 1: Prepare the agentic prompt
            system_prompt = self._get_system_prompt()
            tools_description = self._get_tools_description()
            
            # Step 2: Create the research plan
            plan_prompt = f"""
{system_prompt}

Available Tools:
{tools_description}

User Request: {query}

Please analyze this request and create a research plan. What tools will you use to gather the necessary information?
            """
            
            # Step 3: Get initial response from AI
            logger.info("🧠 Agent is thinking about research plan...")
            
            # For demo purposes, we'll simulate the agent's planning
            research_plan = self._simulate_agent_planning(query)
            
            # Step 4: Execute the plan
            results = self._execute_research_plan(research_plan, query)
            
            # Step 5: Generate insights
            insights = self._generate_insights(results, query)
            
            # Step 6: Format response
            response = self._format_response(results, insights)
            
            logger.info("✅ Research completed successfully")
            return response
        
        except Exception as e:
            logger.error(f"❌ Research failed: {e}")
            return f"Error during research: {str(e)}"
    
    def _get_system_prompt(self) -> str:
        """Get the system prompt that defines the agent's behavior."""
        return f"""
You are {self.name}, an expert market research and business intelligence agent.

Your Purpose:
{self.description}

Your Capabilities:
- Analyze companies and industries
- Research market trends and competitive landscapes
- Gather latest news and developments
- Generate comprehensive business intelligence reports
- Identify market opportunities and threats

Your Approach:
1. Break down complex requests into specific research tasks
2. Use available tools strategically to gather data
3. Synthesize findings into actionable insights
4. Present information clearly and professionally

Remember: You are thorough, accurate, and focused on providing valuable business intelligence.
        """
    
    def _get_tools_description(self) -> str:
        """Generate description of available tools for the agent."""
        description = ""
        for tool_name, tool_info in AVAILABLE_TOOLS.items():
            description += f"\n- {tool_name}: {tool_info['description']}"
        return description
    
    def _simulate_agent_planning(self, query: str) -> Dict[str, List[str]]:
        """
        Simulate agent planning (in production, this would be from the AI model).
        
        This demonstrates how an agent would break down a complex request
        into individual tool calls.
        """
        plan = {
            "steps": [],
            "tools_to_use": [],
        }
        
        query_lower = query.lower()
        
        # Detect what the user wants to research
        if "research" in query_lower or "analyze" in query_lower:
            if any(word in query_lower for word in ["company", "apple", "google", "microsoft"]):
                plan["tools_to_use"].append("search_company_info")
                plan["steps"].append("Search for company information")
            
            if any(word in query_lower for word in ["market", "trends", "industry"]):
                plan["tools_to_use"].append("analyze_market_trends")
                plan["steps"].append("Analyze market trends")
            
            if any(word in query_lower for word in ["competitor", "competition"]):
                plan["tools_to_use"].append("search_competitor_analysis")
                plan["steps"].append("Analyze competitors")
            
            if any(word in query_lower for word in ["news", "latest", "recent"]):
                plan["tools_to_use"].append("search_latest_news")
                plan["steps"].append("Search for latest news")
            
            if any(word in query_lower for word in ["report", "generate", "create"]):
                plan["tools_to_use"].append("generate_market_report")
                plan["steps"].append("Generate comprehensive report")
        
        # Default research tools if nothing specific matched
        if not plan["tools_to_use"]:
            plan["tools_to_use"] = [
                "search_company_info",
                "analyze_market_trends",
                "search_latest_news",
                "generate_market_report",
            ]
            plan["steps"] = [
                "Search for company information",
                "Analyze market trends",
                "Search for latest news",
                "Generate comprehensive report",
            ]
        
        return plan
    
    def _execute_research_plan(self, plan: Dict[str, Any], query: str) -> Dict[str, Any]:
        """
        Execute the research plan by calling appropriate tools.
        
        Args:
            plan: Research plan with tools to use
            query: Original user query
        
        Returns:
            Dictionary with research results
        """
        results = {
            "query": query,
            "timestamp": datetime.now().isoformat(),
            "data": {},
        }
        
        # Extract company name from query
        company = self._extract_company_name(query)
        market = self._extract_market(query, company)
        
        logger.info(f"🎯 Executing research for: {company}")
        
        # Execute each tool in the plan
        for tool_name in plan.get("tools_to_use", []):
            try:
                logger.info(f"🔧 Using tool: {tool_name}")
                
                if tool_name == "search_company_info":
                    results["data"]["company_info"] = ResearchTools.search_company_info(company)
                
                elif tool_name == "analyze_market_trends":
                    results["data"]["market_trends"] = ResearchTools.analyze_market_trends(
                        market or company
                    )
                
                elif tool_name == "search_competitor_analysis":
                    results["data"]["competitor_analysis"] = (
                        ResearchTools.search_competitor_analysis(company)
                    )
                
                elif tool_name == "search_latest_news":
                    results["data"]["latest_news"] = ResearchTools.search_latest_news(company)
                
                elif tool_name == "generate_market_report":
                    results["data"]["report"] = ResearchTools.generate_market_report(
                        company, market or company
                    )
            
            except Exception as e:
                logger.error(f"❌ Tool execution failed for {tool_name}: {e}")
                results["data"][tool_name] = {"error": str(e)}
        
        return results
    
    def _generate_insights(self, results: Dict[str, Any], query: str) -> str:
        """
        Generate insights from research results.
        
        Args:
            results: Research results
            query: Original query
        
        Returns:
            Formatted insights
        """
        insights = "📊 RESEARCH INSIGHTS:\n"
        insights += "=" * 60 + "\n\n"
        
        # Extract and present key findings
        data = results.get("data", {})
        
        if "company_info" in data:
            company_data = data["company_info"].get("data", {})
            insights += f"🏢 COMPANY OVERVIEW:\n"
            insights += f"  • Founded: {company_data.get('founded', 'N/A')}\n"
            insights += f"  • Headquarters: {company_data.get('headquarters', 'N/A')}\n"
            insights += f"  • Employees: {company_data.get('employees', 'N/A')}\n"
            insights += f"  • Industry: {company_data.get('industry', 'N/A')}\n"
            insights += f"  • Market Cap: {company_data.get('market_cap', 'N/A')}\n\n"
        
        if "market_trends" in data:
            trends_data = data["market_trends"].get("data", {})
            insights += f"📈 MARKET TRENDS:\n"
            insights += f"  • Growth Rate: {trends_data.get('growth_rate', 'N/A')}\n"
            insights += f"  • Market Size: {trends_data.get('market_size', 'N/A')}\n"
            if "key_trends" in trends_data:
                insights += "  • Key Trends:\n"
                for trend in trends_data["key_trends"][:3]:
                    insights += f"    - {trend}\n"
            insights += "\n"
        
        if "latest_news" in data:
            news_data = data["latest_news"].get("articles", [])
            insights += f"📰 LATEST NEWS ({len(news_data)} articles):\n"
            for article in news_data[:3]:
                insights += f"  • {article.get('title', 'N/A')} ({article.get('source', 'N/A')})\n"
            insights += "\n"
        
        if "report" in data:
            report_data = data["report"].get("report", {})
            insights += f"📄 REPORT GENERATED:\n"
            insights += f"  • Title: {report_data.get('title', 'N/A')}\n"
            insights += f"  • Date: {report_data.get('date', 'N/A')}\n"
        
        insights += "\n" + "=" * 60 + "\n"
        
        return insights
    
    def _extract_company_name(self, query: str) -> str:
        """Extract company name from query."""
        # Simple extraction - in production, use NLP
        companies = ["Apple", "Google", "Microsoft", "Amazon", "Tesla", "Meta", "Netflix"]
        for company in companies:
            if company.lower() in query.lower():
                return company
        
        # If no known company found, try to extract from query
        words = query.split()
        return words[-1] if words else "Company"
    
    def _extract_market(self, query: str, company: str = "") -> str:
        """Extract market/industry from query."""
        if "market" in query.lower():
            # Extract after "market"
            parts = query.lower().split("market")
            if len(parts) > 1:
                return parts[1].strip().split()[0] if parts[1].strip() else ""
        
        return f"{company} market"
    
    def _format_response(self, results: Dict[str, Any], insights: str) -> str:
        """Format the final response."""
        response = "🤖 MARKET RESEARCH AGENT REPORT\n"
        response += "=" * 60 + "\n\n"
        response += f"Research Request: {results['query']}\n"
        response += f"Timestamp: {results['timestamp']}\n"
        response += f"Agent: {self.name}\n\n"
        response += insights
        response += "\n✅ Research completed successfully!\n"
        
        # Store results for later use
        self.research_results = results
        
        return response
    
    def interactive_chat(self):
        """Run interactive chat mode with the agent."""
        print("\n" + "=" * 60)
        print(f"🤖 Welcome to {self.name}")
        print(f"📊 {self.description}")
        print("=" * 60)
        print("\nType your research requests or 'exit' to quit:\n")
        
        while True:
            try:
                query = input("🔍 Your research request: ").strip()
                
                if query.lower() == "exit":
                    print("\n👋 Thank you for using the Market Research Agent!")
                    break
                
                if not query:
                    print("❌ Please enter a research request\n")
                    continue
                
                response = self.research(query)
                print("\n" + response + "\n")
            
            except KeyboardInterrupt:
                print("\n\n👋 Agent shutting down...")
                break
            except Exception as e:
                logger.error(f"Error in chat: {e}")
                print(f"❌ Error: {e}\n")


# ===== Main Demo Function =====

def demo_research():
    """Run a demo of the market research agent."""
    try:
        # Initialize agent
        print("\n🚀 Initializing Market Research Agent...")
        agent = MarketResearchAgent()
        
        # Example research request
        query = "Research Apple Inc, analyze the smartphone market, identify key competitors, and generate a market report"
        
        print(f"\n📝 Research Query: {query}\n")
        
        # Execute research
        result = agent.research(query)
        print(result)
        
        return agent
    
    except Exception as e:
        logger.error(f"Demo failed: {e}")
        print(f"❌ Error: {e}")
        return None


if __name__ == "__main__":
    agent = demo_research()
