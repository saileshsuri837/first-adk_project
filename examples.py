"""
Example use cases and advanced usage patterns for the Market Research Agent.

This file demonstrates different ways to use the AI agent for various
real-world scenarios.
"""

from agents.market_researcher import MarketResearchAgent
from tools.web_tools import ResearchTools
import logging

logger = logging.getLogger(__name__)


# ===== Example 1: Simple Company Research =====

def example_company_research():
    """Example: Research a single company."""
    print("\n" + "=" * 70)
    print("📌 Example 1: Single Company Research")
    print("=" * 70 + "\n")
    
    agent = MarketResearchAgent()
    
    # Simple research request
    query = "Tell me about Tesla Inc"
    result = agent.research(query)
    print(result)


# ===== Example 2: Competitive Analysis =====

def example_competitive_analysis():
    """Example: Analyze competitors in a market."""
    print("\n" + "=" * 70)
    print("📌 Example 2: Competitive Analysis")
    print("=" * 70 + "\n")
    
    agent = MarketResearchAgent()
    
    # Competitive analysis request
    query = (
        "Compare Apple, Google, and Microsoft in the cloud computing market. "
        "What are their strengths and weaknesses?"
    )
    result = agent.research(query)
    print(result)


# ===== Example 3: Market Opportunity Research =====

def example_market_opportunity():
    """Example: Identify market opportunities."""
    print("\n" + "=" * 70)
    print("📌 Example 3: Market Opportunity Research")
    print("=" * 70 + "\n")
    
    agent = MarketResearchAgent()
    
    # Market opportunity research
    query = (
        "Research the AI market, identify growth opportunities, "
        "and analyze key players"
    )
    result = agent.research(query)
    print(result)


# ===== Example 4: Trend Analysis =====

def example_trend_analysis():
    """Example: Analyze industry trends."""
    print("\n" + "=" * 70)
    print("📌 Example 4: Trend Analysis")
    print("=" * 70 + "\n")
    
    agent = MarketResearchAgent()
    
    # Trend analysis request
    query = "What are the latest trends in the technology sector?"
    result = agent.research(query)
    print(result)


# ===== Example 5: Using Tools Directly =====

def example_direct_tool_usage():
    """Example: Use tools directly without the agent."""
    print("\n" + "=" * 70)
    print("📌 Example 5: Direct Tool Usage")
    print("=" * 70 + "\n")
    
    # You can also use tools directly for specific tasks
    
    print("🔍 Searching company information...")
    company_data = ResearchTools.search_company_info("Apple")
    print(f"Company: {company_data['data']['company']}")
    print(f"Industry: {company_data['data']['industry']}")
    print(f"Market Cap: {company_data['data']['market_cap']}\n")
    
    print("📊 Analyzing market trends...")
    trends = ResearchTools.analyze_market_trends("smartphone market")
    print(f"Market Size: {trends['data']['market_size']}")
    print(f"Growth Rate: {trends['data']['growth_rate']}\n")
    
    print("📰 Searching latest news...")
    news = ResearchTools.search_latest_news("Apple", days_back=7)
    print(f"Found {len(news['articles'])} articles")
    for article in news['articles'][:2]:
        print(f"  - {article['title']} ({article['source']})")


# ===== Example 6: Custom Agent with Specific Focus =====

def example_custom_agent_workflow():
    """Example: Custom workflow for specific business use case."""
    print("\n" + "=" * 70)
    print("📌 Example 6: Custom Agent Workflow")
    print("=" * 70 + "\n")
    
    # This example shows how to create a specialized workflow
    # for a specific business use case
    
    agent = MarketResearchAgent()
    
    companies_to_research = ["Apple", "Microsoft", "Google"]
    
    print("Researching multiple companies...\n")
    
    for company in companies_to_research:
        query = f"Research {company} and provide key market insights"
        print(f"\n📍 Researching {company}...")
        
        result = agent.research(query)
        
        # In production, you would store these results
        # in a database or send them via email


# ===== Example 7: Report Generation Workflow =====

def example_report_generation():
    """Example: Generate and export a comprehensive report."""
    print("\n" + "=" * 70)
    print("📌 Example 7: Report Generation")
    print("=" * 70 + "\n")
    
    agent = MarketResearchAgent()
    
    # Complex research request that results in a comprehensive report
    query = (
        "Analyze the e-commerce market. Include market size, growth trends, "
        "key players, competitive landscape, and opportunities for new entrants."
    )
    
    result = agent.research(query)
    print(result)
    
    # In production, you could:
    # - Export to PDF or Word
    # - Save to database
    # - Send via email
    # - Publish to dashboard


# ===== Example 8: Interactive Research Session =====

def example_interactive_session():
    """Example: Multi-turn research conversation."""
    print("\n" + "=" * 70)
    print("📌 Example 8: Interactive Research Session")
    print("=" * 70)
    print("Entering interactive mode for research...\n")
    
    agent = MarketResearchAgent()
    agent.interactive_chat()


# ===== Example 9: Batch Research =====

def example_batch_research():
    """Example: Research multiple companies in a batch."""
    print("\n" + "=" * 70)
    print("📌 Example 9: Batch Research")
    print("=" * 70 + "\n")
    
    agent = MarketResearchAgent()
    
    research_queries = [
        "Analyze Amazon's cloud business (AWS)",
        "Research Google's AI strategy and investments",
        "Evaluate Microsoft's enterprise software dominance",
    ]
    
    results = {}
    
    for i, query in enumerate(research_queries, 1):
        print(f"\n📝 Query {i}/{ len(research_queries)}: {query}")
        print("-" * 70)
        
        result = agent.research(query)
        results[query] = result
        
        print(result)
    
    print(f"\n✅ Completed batch research ({len(results)} queries)")


# ===== Example 10: Domain-Specific Research =====

def example_domain_specific():
    """Example: Research specific industry domains."""
    print("\n" + "=" * 70)
    print("📌 Example 10: Domain-Specific Research")
    print("=" * 70 + "\n")
    
    agent = MarketResearchAgent()
    
    domains = {
        "Healthcare": "Research the digital health and telemedicine market",
        "Finance": "Analyze the fintech and blockchain market opportunities",
        "Retail": "Study the e-commerce and retail technology trends",
        "Manufacturing": "Investigate Industry 4.0 and smart manufacturing",
    }
    
    for domain, query in domains.items():
        print(f"\n🏢 Domain: {domain}")
        print(f"   Query: {query}")
        print("-" * 70)
        
        result = agent.research(query)
        # Store or process result
        print("✓ Research complete\n")


# ===== Main Demo Menu =====

def show_examples_menu():
    """Show available examples."""
    print("\n" + "=" * 70)
    print("📚 EXAMPLE USE CASES")
    print("=" * 70)
    print("\nChoose an example to run:\n")
    
    examples = {
        "1": ("Single Company Research", example_company_research),
        "2": ("Competitive Analysis", example_competitive_analysis),
        "3": ("Market Opportunity", example_market_opportunity),
        "4": ("Trend Analysis", example_trend_analysis),
        "5": ("Direct Tool Usage", example_direct_tool_usage),
        "6": ("Custom Workflow", example_custom_agent_workflow),
        "7": ("Report Generation", example_report_generation),
        "8": ("Interactive Session", example_interactive_session),
        "9": ("Batch Research", example_batch_research),
        "10": ("Domain-Specific Research", example_domain_specific),
    }
    
    for key, (name, _) in examples.items():
        print(f"  {key}. {name}")
    
    print("\n  0. Exit")
    print("\n" + "=" * 70)
    
    choice = input("\nEnter your choice (0-10): ").strip()
    
    if choice == "0":
        print("👋 Goodbye!")
        return False
    
    if choice in examples:
        try:
            examples[choice][1]()
        except Exception as e:
            logger.error(f"Example failed: {e}")
            print(f"\n❌ Error running example: {e}")
    else:
        print("❌ Invalid choice")
    
    return True


def run_examples():
    """Run the examples menu."""
    while True:
        if not show_examples_menu():
            break
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🤖 MARKET RESEARCH AGENT - EXAMPLES")
    print("=" * 70)
    
    run_examples()
