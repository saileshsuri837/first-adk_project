"""
Configuration Management for ADK Market Research Agent

This module handles:
- Loading environment variables
- Initializing AI models
- Setting up logging
- Validating configuration
"""

import os
from typing import Literal
from pathlib import Path
import logging
from dotenv import load_dotenv


# Load environment variables from .env file
ENV_FILE = Path(__file__).parent / ".env"
load_dotenv(ENV_FILE)


# ===== Logging Configuration =====
def setup_logging(level: str = "INFO") -> logging.Logger:
    """
    Configure logging for the agent.
    
    Args:
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    
    Returns:
        Configured logger
    """
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("agent.log", mode="a"),
        ],
    )
    return logging.getLogger(__name__)


logger = setup_logging(os.getenv("LOG_LEVEL", "INFO"))


# ===== API Keys Configuration =====
class APIConfig:
    """Manages API keys and credentials."""
    
    @staticmethod
    def get_google_api_key() -> str:
        """Get Google Gemini API key."""
        key = os.getenv("GOOGLE_API_KEY")
        if not key:
            raise ValueError(
                "❌ GOOGLE_API_KEY not found!\n"
                "Get it from: https://aistudio.google.com\n"
                "Then add to .env file: GOOGLE_API_KEY=your_key_here"
            )
        return key
    
    @staticmethod
    def get_anthropic_api_key() -> str:
        """Get Anthropic Claude API key."""
        key = os.getenv("ANTHROPIC_API_KEY")
        if not key:
            logger.warning("⚠️  ANTHROPIC_API_KEY not found. Claude models unavailable.")
        return key or ""
    
    @staticmethod
    def get_openai_api_key() -> str:
        """Get OpenAI API key."""
        key = os.getenv("OPENAI_API_KEY")
        if not key:
            logger.warning("⚠️  OPENAI_API_KEY not found. OpenAI models unavailable.")
        return key or ""


# ===== Agent Configuration =====
class AgentConfig:
    """Configuration for the AI Agent."""
    
    MODEL_TYPE: Literal["google", "anthropic", "openai"] = os.getenv(
        "AGENT_MODEL", "google"
    )
    
    AGENT_NAME: str = os.getenv("AGENT_NAME", "ResearcherBot")
    
    AGENT_DESCRIPTION: str = os.getenv(
        "AGENT_DESCRIPTION",
        "An intelligent Market Research and Intelligence Agent"
    )
    
    MAX_ITERATIONS: int = int(os.getenv("MAX_ITERATIONS", "10"))
    
    TIMEOUT_SECONDS: int = int(os.getenv("TIMEOUT_SECONDS", "300"))
    
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    TEST_MODE: bool = os.getenv("TEST_MODE", "False").lower() == "true"


# ===== Email Configuration =====
class EmailConfig:
    """Configuration for email sending (optional)."""
    
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SENDER_EMAIL: str = os.getenv("SENDER_EMAIL", "")
    SENDER_PASSWORD: str = os.getenv("SENDER_PASSWORD", "")
    
    @staticmethod
    def is_configured() -> bool:
        """Check if email is properly configured."""
        return bool(
            os.getenv("SENDER_EMAIL") 
            and os.getenv("SENDER_PASSWORD")
        )


# ===== Model Selection =====
def get_model_config() -> dict:
    """
    Get configuration for the selected AI model.
    
    Returns:
        Dictionary with model configuration
    """
    model_type = AgentConfig.MODEL_TYPE
    
    if model_type == "google":
        return {
            "type": "google",
            "model": "gemini-pro",
            "api_key": APIConfig.get_google_api_key(),
        }
    elif model_type == "anthropic":
        api_key = APIConfig.get_anthropic_api_key()
        if not api_key:
            raise ValueError("Anthropic API key not configured")
        return {
            "type": "anthropic",
            "model": "claude-3-sonnet-20240229",
            "api_key": api_key,
        }
    elif model_type == "openai":
        api_key = APIConfig.get_openai_api_key()
        if not api_key:
            raise ValueError("OpenAI API key not configured")
        return {
            "type": "openai",
            "model": "gpt-4",
            "api_key": api_key,
        }
    else:
        raise ValueError(f"Unknown model type: {model_type}")


# ===== Logging Configuration =====
if __name__ == "__main__":
    logger.info("✅ Configuration loaded successfully")
    logger.info(f"📊 Agent: {AgentConfig.AGENT_NAME}")
    logger.info(f"🧠 Model: {AgentConfig.MODEL_TYPE}")
    logger.info(f"⏱️  Max Iterations: {AgentConfig.MAX_ITERATIONS}")
    print("\n✨ Configuration is ready!\n")
