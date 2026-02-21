#!/usr/bin/env python3
"""
ADK Project Validator - Verify project setup

This script checks that the project is properly configured and ready to run.
"""

import os
import sys
from pathlib import Path

def print_header(text):
    """Print a formatted header."""
    print(f"\n{'=' * 70}")
    print(f"  {text}")
    print(f"{'=' * 70}\n")

def check_directory_structure():
    """Check that all required directories exist."""
    print("📁 Checking directory structure...")
    
    required_dirs = [
        "agents",
        "tools",
        "tests",
    ]
    
    all_exist = True
    for dir_name in required_dirs:
        path = Path(dir_name)
        if path.exists():
            print(f"  ✅ {dir_name}/")
        else:
            print(f"  ❌ {dir_name}/ - MISSING")
            all_exist = False
    
    return all_exist

def check_files():
    """Check that all required files exist."""
    print("\n📄 Checking required files...")
    
    required_files = [
        "main.py",
        "config.py",
        "requirements.txt",
        "README.md",
        ".env.example",
        ".gitignore",
        "QUICKSTART.md",
        "DEPLOYMENT.md",
        "ARCHITECTURE.md",
        "examples.py",
        "agents/market_researcher.py",
        "tools/web_tools.py",
        "tests/test_agent.py",
    ]
    
    all_exist = True
    for file_name in required_files:
        path = Path(file_name)
        if path.exists():
            size = path.stat().st_size
            print(f"  ✅ {file_name} ({size} bytes)")
        else:
            print(f"  ❌ {file_name} - MISSING")
            all_exist = False
    
    return all_exist

def check_environment():
    """Check Python environment and dependencies."""
    print("\n🐍 Checking Python environment...")
    
    python_version = sys.version_info
    print(f"  Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major >= 3 and python_version.minor >= 8:
        print("  ✅ Python version is compatible")
        compatible = True
    else:
        print("  ❌ Python 3.8+ required")
        compatible = False
    
    return compatible

def check_env_file():
    """Check if .env file exists."""
    print("\n🔐 Checking configuration...")
    
    env_path = Path(".env")
    example_path = Path(".env.example")
    
    if example_path.exists():
        print(f"  ✅ .env.example exists")
    else:
        print(f"  ❌ .env.example not found")
        return False
    
    if env_path.exists():
        print(f"  ✅ .env file configured")
        
        try:
            with open(env_path) as f:
                content = f.read()
                if "GOOGLE_API_KEY" in content and "your_" not in content:
                    print("  ✅ Google API key appears to be set")
                    return True
                else:
                    print("  ⚠️  GOOGLE_API_KEY not configured (required)")
                    return False
        except Exception as e:
            print(f"  ❌ Error reading .env: {e}")
            return False
    else:
        print("  ⚠️  .env file not found (create from .env.example)")
        return False

def check_imports():
    """Check that key modules can be imported."""
    print("\n📦 Checking Python imports...")
    
    modules_to_check = [
        ("config", "Configuration module"),
        ("tools.web_tools", "Research tools"),
        ("agents.market_researcher", "Market research agent"),
    ]
    
    all_importable = True
    for module_name, description in modules_to_check:
        try:
            __import__(module_name)
            print(f"  ✅ {description} ({module_name})")
        except ImportError as e:
            print(f"  ⚠️  {description} ({module_name}) - Missing dependencies: {e}")
            all_importable = False
        except Exception as e:
            print(f"  ❌ {description} ({module_name}) - Error: {e}")
            all_importable = False
    
    return all_importable

def run_validation():
    """Run all validation checks."""
    print_header("🤖 ADK PROJECT VALIDATOR")
    
    checks = [
        ("Directory Structure", check_directory_structure()),
        ("Required Files", check_files()),
        ("Python Environment", check_environment()),
        ("Configuration", check_env_file()),
    ]
    
    # Try to check imports (may fail if dependencies not installed)
    try:
        checks.append(("Module Imports", check_imports()))
    except Exception as e:
        print(f"\n⚠️  Could not check imports (dependencies might not be installed)")
        checks.append(("Module Imports", False))
    
    # Summary
    print_header("📊 VALIDATION SUMMARY")
    
    all_passed = True
    for check_name, passed in checks:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status}: {check_name}")
        if not passed:
            all_passed = False
    
    print(f"\n{'=' * 70}")
    
    if all_passed:
        print("\n✨ All checks passed! Project is ready to run:\n")
        print("  python main.py                    # Run demo")
        print("  python main.py --interactive      # Chat mode")
        print('  python main.py --research "query" # Custom research\n')
    else:
        print("\n❌ Some checks failed. Please fix the issues above.\n")
        print("Quick fixes:")
        print("  1. Create .env from .env.example: cp .env.example .env")
        print("  2. Add your API key to .env file")
        print("  3. Install dependencies: pip install -r requirements.txt")
        print("  4. Activate virtual environment: source venv/bin/activate\n")
    
    return all_passed

if __name__ == "__main__":
    success = run_validation()
    sys.exit(0 if success else 1)
