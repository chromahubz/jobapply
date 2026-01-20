# JobApply - AI-Powered Job Application Assistant

Automate your job applications with AI! Paste job posting URLs, scrape descriptions, and generate tailored cover letters, emails, and LinkedIn messages using Groq LLM.

## Features

- 📋 **URL-based scraping**: Paste any job posting URL to extract details
- 🤖 **AI-powered generation**: Uses Groq LLM to create personalized responses
- ✉️ **Multiple formats**: Cover letters, emails, LinkedIn messages
- 💾 **Auto-save**: All outputs saved to organized files
- 🎨 **Interactive CLI**: Beautiful terminal interface with Rich

## Quick Start

### 1. Installation

```bash
# Clone the repository
cd jobapply

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browsers (for advanced scraping)
playwright install chromium
```

### 2. Configuration

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` and add your details:

```env
# Get your free API key from https://console.groq.com
GROQ_API_KEY=gsk_your_api_key_here

# Your personal information
YOUR_NAME="John Doe"
YOUR_EMAIL="john.doe@email.com"
YOUR_PHONE="+1234567890"
YOUR_LINKEDIN="https://linkedin.com/in/johndoe"

# Path to your resume
RESUME_PATH="./resume.txt"
```

### 3. Add Your Resume

Create a `resume.txt` file with your resume/CV text, or paste it when prompted.

### 4. Run

```bash
python main.py
```

## Usage

1. **Paste a job URL** when prompted
2. **Review scraped content** (edit if needed)
3. **Choose what to generate**:
   - Cover letter
   - Application email
   - Recruiter outreach email
   - LinkedIn message
   - All of the above

4. **Find your outputs** in `./applications/` folder

## Supported Job Boards

- LinkedIn
- Indeed
- Greenhouse
- Any job posting website (generic scraper)

## Tech Stack

- **Python 3.10+**
- **Groq API** - Fast LLM inference
- **BeautifulSoup4** - Web scraping
- **Playwright** - Advanced scraping (optional)
- **Rich** - Beautiful CLI interface

## File Structure

```
jobapply/
├── main.py              # Main CLI application
├── scraper.py           # Job posting scraper
├── llm_generator.py     # Groq LLM integration
├── config.py            # Configuration management
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── resume.txt           # Your resume (create this)
└── applications/        # Generated outputs (auto-created)
```

## Tips

- **Be specific**: Better job descriptions = better AI responses
- **Review outputs**: Always review and customize AI-generated content
- **Update resume**: Keep your resume.txt current for best results
- **Save time**: Generate all formats at once, then pick the best

## Groq API

Get a free API key at [console.groq.com](https://console.groq.com). Free tier includes:
- Fast inference with Llama models
- Generous rate limits
- No credit card required

## License

MIT License - feel free to use and modify!

## Contributing

Pull requests welcome! Feel free to:
- Add more job board scrapers
- Improve prompt engineering
- Add new output formats
- Enhance UI/UX

---

**Note**: This tool is for personal use to streamline your job search. Always review and personalize AI-generated content before sending.
