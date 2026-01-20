#!/usr/bin/env python3
"""
JobApply - Job Application Assistant
Paste job URLs, scrape descriptions, and generate optimized responses using Groq LLM
"""

import sys
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.markdown import Markdown

from config import Config
from scraper import JobScraper
from llm_generator import ResponseGenerator


console = Console()


def print_banner():
    """Print welcome banner"""
    banner = """
    ╔═══════════════════════════════════════╗
    ║       JobApply Assistant v1.0         ║
    ║   AI-Powered Job Application Tool     ║
    ╚═══════════════════════════════════════╝
    """
    console.print(banner, style="bold cyan")


def save_output(job_title: str, company: str, content: str, output_type: str):
    """Save generated content to file"""
    # Create safe filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = "".join(c for c in job_title if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_company = "".join(c for c in company if c.isalnum() or c in (' ', '-', '_')).strip()

    filename = f"{timestamp}_{safe_company}_{safe_title}_{output_type}.txt"
    filepath = Config.OUTPUT_DIR / filename

    filepath.write_text(content, encoding='utf-8')
    console.print(f"✓ Saved to: {filepath}", style="green")


def main():
    """Main application loop"""
    print_banner()

    # Validate configuration
    try:
        Config.validate()
    except ValueError as e:
        console.print(f"[red]Configuration Error: {e}[/red]")
        console.print("\n[yellow]Please create a .env file based on .env.example[/yellow]")
        return

    # Load resume
    resume_text = Config.load_resume()
    if not resume_text:
        console.print("[yellow]Warning: No resume found. You can paste it manually or add it to resume.txt[/yellow]\n")
        if Confirm.ask("Do you want to paste your resume text now?"):
            console.print("[cyan]Paste your resume (press Ctrl+D or Ctrl+Z when done):[/cyan]")
            resume_lines = []
            try:
                while True:
                    line = input()
                    resume_lines.append(line)
            except EOFError:
                pass
            resume_text = "\n".join(resume_lines)

    scraper = JobScraper()
    generator = ResponseGenerator()

    console.print("\n[green]Ready! Paste job posting URLs to get started.[/green]\n")

    while True:
        # Get job URL
        url = Prompt.ask("\n[bold cyan]Enter job posting URL[/bold cyan] (or 'quit' to exit)")

        if url.lower() in ['quit', 'exit', 'q']:
            console.print("[yellow]Goodbye![/yellow]")
            break

        if not url.startswith('http'):
            console.print("[red]Please enter a valid URL starting with http:// or https://[/red]")
            continue

        # Scrape job posting
        console.print("\n[cyan]Scraping job posting...[/cyan]")
        job_info = scraper.scrape(url)

        # Display job info
        console.print(Panel(
            f"[bold]Title:[/bold] {job_info['title']}\n"
            f"[bold]Company:[/bold] {job_info['company']}\n"
            f"[bold]Description:[/bold] {job_info['description'][:200]}...",
            title="Job Information",
            border_style="green"
        ))

        # Allow manual editing
        if Confirm.ask("\nDo you want to manually edit/paste the job description?"):
            console.print("[cyan]Paste the job description (press Ctrl+D or Ctrl+Z when done):[/cyan]")
            desc_lines = []
            try:
                while True:
                    line = input()
                    desc_lines.append(line)
            except EOFError:
                pass
            job_info['description'] = "\n".join(desc_lines)

        # Choose what to generate
        console.print("\n[bold cyan]What would you like to generate?[/bold cyan]")
        console.print("1. Cover Letter")
        console.print("2. Email (Application)")
        console.print("3. Email (Recruiter Outreach)")
        console.print("4. LinkedIn Message")
        console.print("5. All of the above")

        choice = Prompt.ask("Enter choice", choices=["1", "2", "3", "4", "5"], default="5")

        console.print("\n[cyan]Generating with Groq LLM...[/cyan]\n")

        # Generate requested content
        if choice in ["1", "5"]:
            cover_letter = generator.generate_cover_letter(job_info, resume_text)
            console.print(Panel(Markdown(cover_letter), title="Cover Letter", border_style="blue"))
            save_output(job_info['title'], job_info['company'], cover_letter, "cover_letter")

        if choice in ["2", "5"]:
            email = generator.generate_email(job_info, resume_text, "application")
            console.print(Panel(email, title="Application Email", border_style="blue"))
            save_output(job_info['title'], job_info['company'], email, "email_application")

        if choice in ["3", "5"]:
            recruiter_email = generator.generate_email(job_info, resume_text, "recruiter")
            console.print(Panel(recruiter_email, title="Recruiter Email", border_style="blue"))
            save_output(job_info['title'], job_info['company'], recruiter_email, "email_recruiter")

        if choice in ["4", "5"]:
            linkedin_msg = generator.generate_linkedin_message(job_info, resume_text)
            console.print(Panel(linkedin_msg, title="LinkedIn Message", border_style="blue"))
            save_output(job_info['title'], job_info['company'], linkedin_msg, "linkedin_message")

        console.print("\n[green]✓ All outputs saved to ./applications/ folder[/green]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user. Goodbye![/yellow]")
        sys.exit(0)
