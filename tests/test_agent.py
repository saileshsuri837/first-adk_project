"""
Unit tests for the Market Research AI Agent

These tests verify that:
1. Agent initializes correctly
2. Tools execute as expected
3. Research planning works
4. Response formatting is correct
"""

import unittest
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from tools.web_tools import ResearchTools, AVAILABLE_TOOLS
from config import AgentConfig


class TestResearchTools(unittest.TestCase):
    """Test research tools."""
    
    def test_company_search(self):
        """Test company information search."""
        result = ResearchTools.search_company_info("Apple")
        
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        self.assertIn("data", result)
        self.assertIn("company", result["data"])
    
    def test_market_analysis(self):
        """Test market trend analysis."""
        result = ResearchTools.analyze_market_trends("smartphone market")
        
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        self.assertIn("data", result)
        self.assertIn("market_size", result["data"])
    
    def test_news_search(self):
        """Test news search."""
        result = ResearchTools.search_latest_news("Apple", days_back=30)
        
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        self.assertIn("articles", result)
    
    def test_report_generation(self):
        """Test report generation."""
        result = ResearchTools.generate_market_report("Apple", "smartphone")
        
        self.assertIn("status", result)
        self.assertEqual(result["status"], "success")
        self.assertIn("report", result)
        self.assertIn("title", result["report"])


class TestAvailableTools(unittest.TestCase):
    """Test tool availability and configuration."""
    
    def test_tools_configured(self):
        """Test that tools are properly configured."""
        self.assertGreater(len(AVAILABLE_TOOLS), 0)
    
    def test_tool_descriptions(self):
        """Test that all tools have descriptions."""
        for tool_name, tool_info in AVAILABLE_TOOLS.items():
            self.assertIn("description", tool_info)
            self.assertIn("function", tool_info)
            self.assertTrue(len(tool_info["description"]) > 0)
    
    def test_required_tools(self):
        """Test that required tools exist."""
        required_tools = [
            "search_company_info",
            "analyze_market_trends",
            "generate_market_report",
        ]
        
        for tool in required_tools:
            self.assertIn(tool, AVAILABLE_TOOLS)


class TestAgentConfiguration(unittest.TestCase):
    """Test agent configuration."""
    
    def test_agent_name(self):
        """Test agent has a name."""
        self.assertIsNotNone(AgentConfig.AGENT_NAME)
        self.assertGreater(len(AgentConfig.AGENT_NAME), 0)
    
    def test_agent_model_type(self):
        """Test agent has valid model type."""
        valid_types = ["google", "anthropic", "openai"]
        self.assertIn(AgentConfig.MODEL_TYPE, valid_types)
    
    def test_max_iterations(self):
        """Test max iterations is reasonable."""
        self.assertGreater(AgentConfig.MAX_ITERATIONS, 0)
        self.assertLessEqual(AgentConfig.MAX_ITERATIONS, 100)


class TestEmailConfig(unittest.TestCase):
    """Test email configuration."""
    
    def test_email_config_structure(self):
        """Test email configuration is properly structured."""
        from config import EmailConfig
        
        self.assertIsNotNone(EmailConfig.SMTP_SERVER)
        self.assertGreater(EmailConfig.SMTP_PORT, 0)


def run_tests():
    """Run all tests."""
    print("\n" + "=" * 70)
    print("🧪 Running ADK Project Tests")
    print("=" * 70 + "\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add tests
    suite.addTests(loader.loadTestsFromTestCase(TestResearchTools))
    suite.addTests(loader.loadTestsFromTestCase(TestAvailableTools))
    suite.addTests(loader.loadTestsFromTestCase(TestAgentConfiguration))
    suite.addTests(loader.loadTestsFromTestCase(TestEmailConfig))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
    print("=" * 70 + "\n")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
