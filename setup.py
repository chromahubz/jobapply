#!/usr/bin/env python3
"""
Easy setup script for JobApply
Automates installation and configuration
"""

import os
import sys
import subprocess
from pathlib import Path

def print_banner():
    print("\n" + "="*60)
    print("   JobApply - Easy Setup Script")
    print("="*60 + "\n")

def check_python_version():
    """Ensure Python 3.10+"""
    if sys.version_info < (3, 10):
        print("❌ Python 3.10 or higher is required")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    print("✓ Python version OK")

def install_dependencies():
    """Install required packages"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"])
        print("✓ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def setup_env_file():
    """Interactive .env file setup"""
    print("\n⚙️  Setting up configuration...")

    env_path = Path(".env")

    if env_path.exists():
        response = input("\n.env file already exists. Overwrite? (y/N): ").strip().lower()
        if response != 'y':
            print("✓ Keeping existing .env file")
            return

    print("\n" + "="*60)
    print("📝 Let's set up your configuration")
    print("="*60)

    # Groq API Key
    print("\n🔑 GROQ API KEY")
    print("   Get your FREE API key at: https://console.groq.com/keys")
    print("   (Takes 2 minutes - no credit card required!)")
    print()
    groq_key = input("   Enter your Groq API key (or press Enter to set later): ").strip()
    if not groq_key:
        groq_key = "YOUR_GROQ_API_KEY_HERE"
        print("   ⚠️  Remember to add your key to .env before running!")

    # Personal Information
    print("\n👤 YOUR INFORMATION")
    your_name = input("   Your full name: ").strip() or "Your Name"
    your_email = input("   Your email: ").strip() or "your.email@example.com"
    your_phone = input("   Your phone (optional): ").strip() or "+1234567890"
    your_linkedin = input("   Your LinkedIn URL (optional): ").strip() or "https://linkedin.com/in/yourprofile"

    # Write .env file
    env_content = f"""# Groq API Configuration
GROQ_API_KEY={groq_key}

# Your Personal Information
YOUR_NAME="{your_name}"
YOUR_EMAIL="{your_email}"
YOUR_PHONE="{your_phone}"
YOUR_LINKEDIN="{your_linkedin}"

# Path to your resume/CV
RESUME_PATH="./resume.txt"
"""

    with open(".env", "w") as f:
        f.write(env_content)

    print("\n✓ Configuration saved to .env")

def setup_resume():
    """Help user set up resume"""
    print("\n📄 RESUME SETUP")
    resume_path = Path("resume.txt")

    if resume_path.exists() and resume_path.stat().st_size > 100:
        print("   ✓ resume.txt already exists")
        return

    print("   You need to add your resume for AI to generate personalized applications")
    print()
    response = input("   Would you like to paste your resume now? (y/N): ").strip().lower()

    if response == 'y':
        print("\n   Paste your resume below (press Ctrl+D when done on Linux/Mac, Ctrl+Z on Windows):")
        print("   " + "-"*56)
        try:
            resume_lines = []
            while True:
                try:
                    line = input()
                    resume_lines.append(line)
                except EOFError:
                    break

            resume_content = "\n".join(resume_lines)
            with open("resume.txt", "w") as f:
                f.write(resume_content)
            print("\n   ✓ Resume saved to resume.txt")
        except KeyboardInterrupt:
            print("\n   ⚠️  Resume setup skipped")
    else:
        print("   ⚠️  Remember to edit resume.txt before running the app!")

def create_applications_dir():
    """Create output directory"""
    Path("applications").mkdir(exist_ok=True)
    print("✓ Output directory created: ./applications/")

def print_final_instructions():
    """Show how to run the app"""
    print("\n" + "="*60)
    print("🎉 Setup Complete!")
    print("="*60)
    print("\n📋 NEXT STEPS:\n")

    env_path = Path(".env")
    if env_path.exists():
        with open(env_path) as f:
            content = f.read()
            if "YOUR_GROQ_API_KEY_HERE" in content:
                print("   1. Get your FREE Groq API key:")
                print("      → Visit: https://console.groq.com/keys")
                print("      → Sign up (2 minutes, no credit card)")
                print("      → Create API key")
                print("      → Add it to .env file")
                print()

    resume_path = Path("resume.txt")
    if not resume_path.exists() or resume_path.stat().st_size < 100:
        print("   2. Add your resume to resume.txt")
        print()

    print("   3. Run the app:")
    print("      → python main.py")
    print()
    print("   4. Paste job URLs and let AI do the work!")
    print()
    print("="*60)
    print("\n💡 TIP: Keep this window open and visit console.groq.com in your browser")
    print()

def main():
    print_banner()

    try:
        # Step 1: Check Python version
        check_python_version()

        # Step 2: Install dependencies
        install_dependencies()

        # Step 3: Create directories
        create_applications_dir()

        # Step 4: Setup .env
        setup_env_file()

        # Step 5: Setup resume
        setup_resume()

        # Step 6: Final instructions
        print_final_instructions()

    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
