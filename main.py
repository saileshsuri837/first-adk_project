#!/usr/bin/env python3
"""
Market Research AI Agent - Main Entry Point

This script demonstrates the Google Agent Development Kit (ADK) with a
real-world use case: an intelligent market research agent.

Usage:
    python main.py                    # Run demo
    python main.py --interactive      # Chat mode
    python main.py --research "query" # Custom research
    python main.py --web              # Web interface
"""

import sys
import argparse
import logging
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from config import setup_logging, logger, AgentConfig
from agents.market_researcher import MarketResearchAgent
from tools.web_tools import list_tools, get_tool_description

# Configure logging
setup_logging("INFO")


def print_welcome_banner():
    """Print welcome message."""
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                   🤖 MARKET RESEARCH AI AGENT                              ║
║                 Google Agent Development Kit (ADK) Demo                      ║
║                                                                              ║
║  An intelligent agent that researches companies, analyzes markets,          ║
║  and generates business intelligence reports automatically.                 ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_agent_info():
    """Print information about the agent."""
    print("\n📋 AGENT INFORMATION:")
    print("=" * 70)
    print(f"Name: {AgentConfig.AGENT_NAME}")
    print(f"Description: {AgentConfig.AGENT_DESCRIPTION}")
    print(f"Model: {AgentConfig.MODEL_TYPE}")
    print(f"Max Iterations: {AgentConfig.MAX_ITERATIONS}")
    print(f"Timeout: {AgentConfig.TIMEOUT_SECONDS}s")
    print("\n🛠️  AVAILABLE TOOLS:")
    print("-" * 70)
    for tool_name in list_tools():
        print(f"  ✓ {tool_name}")
        print(f"    {get_tool_description(tool_name)}\n")
    print("=" * 70)


def run_demo():
    """Run the demo mode."""
    print_welcome_banner()
    print_agent_info()
    
    print("\n🚀 Starting Demo Research...\n")
    
    try:
        # Initialize agent
        agent = MarketResearchAgent()
        
        # Run example research
        demo_query = (
            "Research Apple Inc, analyze the smartphone market trends, "
            "identify key competitors, and generate a comprehensive market report"
        )
        
        print(f"📌 Research Request: {demo_query}\n")
        print("=" * 70)
        
        # Execute research
        result = agent.research(demo_query)
        print(result)
        
        # Show next steps
        print_next_steps()
    
    except Exception as e:
        logger.error(f"Demo failed: {e}")
        print(f"\n❌ Error running demo: {e}")
        print("\n💡 Troubleshooting:")
        print("  1. Check that you have set up your .env file")
        print("  2. Verify your API keys are valid")
        print("  3. Ensure you have internet connection for API calls")
        sys.exit(1)


def run_interactive():
    """Run interactive chat mode."""
    print_welcome_banner()
    
    try:
        agent = MarketResearchAgent()
        agent.interactive_chat()
    
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    
    except Exception as e:
        logger.error(f"Interactive mode failed: {e}")
        print(f"\n❌ Error: {e}")
        sys.exit(1)


def run_custom_research(query: str):
    """Run custom research query."""
    print_welcome_banner()
    print("\n🔍 Running Custom Research...\n")
    
    try:
        agent = MarketResearchAgent()
        result = agent.research(query)
        print(result)
        print_next_steps()
    
    except Exception as e:
        logger.error(f"Research failed: {e}")
        print(f"❌ Error: {e}")
        sys.exit(1)


def run_web_interface():
    """Run web interface mode."""
    print_welcome_banner()
    print("\n🌐 Starting Web Interface...\n")
    print("⚠️  Web interface is a demonstration feature.")
    print("In production, this would launch a full web dashboard.\n")
    
    try:
        agent = MarketResearchAgent()
        
        print("📊 Example Web Functionality - Agent Status:")
        print(f"  ✓ Agent Name: {agent.name}")
        print(f"  ✓ Status: Ready")
        print(f"  ✓ Available Tools: {len(list_tools())}")
        
        print("\n💡 To test the agent interactively, use:")
        print("  python main.py --interactive")
        
    except Exception as e:
        logger.error(f"Web interface failed: {e}")
        print(f"❌ Error: {e}")
        sys.exit(1)


def print_next_steps():
    """Print suggested next steps."""
    print("\n" + "=" * 70)
    print("\n📚 NEXT STEPS:")
    print("-" * 70)
    print("\n1. 💬 Try Interactive Mode:")
    print("   python main.py --interactive")
    
    print("\n2. 🔍 Custom Research:")
    print('   python main.py --research "Your research query here"')
    
    print("\n3. 📖 Learn More:")
    print("   - Check the README.md for detailed documentation")
    print("   - Review tools/web_tools.py to understand available tools")
    print("   - Edit agents/market_researcher.py to customize behavior")
    
    print("\n4. 🚀 Deploy to Cloud:")
    print("   - Google Vertex AI")
    print("   - Google Cloud Run")
    print("   - AWS Lambda")
    
    print("\n5. 🛠️  Extend the Agent:")
    print("   - Add new tools in tools/web_tools.py")
    print("   - Connect to real APIs (databases, web services)")
    print("   - Chain multiple agents for complex workflows")
    
    print("\n" + "=" * 70 + "\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Market Research AI Agent - Google ADK Demo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                         # Run demo
  python main.py --interactive           # Chat mode
  python main.py --research "Apple Inc"  # Custom query
  python main.py --web                   # Web interface
  python main.py --tools                 # List tools
  python main.py --info                  # Show agent info
        """,
    )
    
    parser.add_argument(
        "--interactive",
        "-i",
        action="store_true",
        help="Run in interactive chat mode",
    )
    
    parser.add_argument(
        "--research",
        "-r",
        type=str,
        help="Run a specific research query",
        metavar="QUERY",
    )
    
    parser.add_argument(
        "--web",
        "-w",
        action="store_true",
        help="Run web interface (demonstration)",
    )
    
    parser.add_argument(
        "--tools",
        "-t",
        action="store_true",
        help="List available tools",
    )
    
    parser.add_argument(
        "--info",
        action="store_true",
        help="Show agent information",
    )
    
    parser.add_argument(
        "--debug",
        "-d",
        action="store_true",
        help="Enable debug logging",
    )
    
    args = parser.parse_args()
    
    # Configure debug logging if requested
    if args.debug:
        setup_logging("DEBUG")
    
    # Route to appropriate mode
    try:
        if args.tools:
            print_welcome_banner()
            print_agent_info()
        
        elif args.info:
            print_welcome_banner()
            print_agent_info()
            print_next_steps()
        
        elif args.interactive:
            run_interactive()
        
        elif args.research:
            run_custom_research(args.research)
        
        elif args.web:
            run_web_interface()
        
        else:
            # Default: run demo
            run_demo()
    
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    
    except Exception as e:
        logger.error(f"Application error: {e}")
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
