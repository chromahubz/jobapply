# JobApply - AI-Powered Job Application Assistant

Automate your job applications with AI! Paste job posting URLs, scrape descriptions, and generate tailored cover letters, emails, and LinkedIn messages using Groq LLM.

## Features

- 📋 **URL-based scraping**: Paste any job posting URL to extract details
- 🤖 **AI-powered generation**: Uses Groq LLM to create personalized responses
- ✉️ **Multiple formats**: Cover letters, emails, LinkedIn messages
- 💾 **Auto-save**: All outputs saved to organized files
- 🎨 **Interactive CLI**: Beautiful terminal interface with Rich

## 🚀 Super Easy Setup (2 Minutes!)

### Option 1: Automatic Setup (Recommended)

```bash
# Run the setup script - it does everything for you!
python3 setup.py
```

The script will:
- ✓ Install all dependencies
- ✓ Ask for your Groq API key (free at console.groq.com)
- ✓ Set up your personal info
- ✓ Help you add your resume
- ✓ Create all necessary folders

Then just run:
```bash
python3 main.py
```

### Option 2: Even Easier (One Command)

**Linux/Mac:**
```bash
./run.sh
```

**Windows:**
```bash
run.bat
```

These scripts automatically run setup if needed, then launch the app!

### Option 3: Manual Setup

If you prefer doing it manually:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Get FREE Groq API key
# Visit: https://console.groq.com/keys
# Sign up → Create API Key → Copy it

# 3. Create .env file
cp .env.example .env
# Edit .env and paste your API key

# 4. Add your resume to resume.txt

# 5. Run
python main.py
```

## 🎨 Two Ways to Use JobApply

### Option A: Web UI (Recommended for Most Users)

Beautiful browser-based interface with Apple design language!

**Linux/Mac:**
```bash
./run_web.sh
```

**Windows:**
```bash
run_web.bat
```

Then open **http://localhost:5000** in your browser.

**Features:**
- 🎨 Clean, modern Apple-inspired design
- 📱 Works on any device with a browser
- ✨ Smooth animations and transitions
- 📋 Easy copy-to-clipboard buttons
- 🎯 Visual step-by-step workflow

### Option B: Command Line (For Power Users)

Terminal-based interface with Rich formatting.

```bash
python main.py
```

or

```bash
./run.sh
```

**Features:**
- ⚡ Fast and lightweight
- 💻 Perfect for terminal enthusiasts
- 🎨 Colored output with Rich library
- ⌨️ Keyboard-driven workflow

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
- **Groq API** - Fast LLM inference (Llama 3.3 70B)
- **Flask** - Web UI framework
- **BeautifulSoup4** - Web scraping
- **Playwright** - Advanced scraping (optional)
- **Rich** - Beautiful CLI interface
- **Apple Design Language** - Modern, clean web UI

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

## 🔑 Getting Your Free Groq API Key

**It takes 2 minutes and requires NO credit card!**

1. Visit [console.groq.com/keys](https://console.groq.com/keys)
2. Sign up with your email
3. Click "Create API Key"
4. Copy the key and paste it in your `.env` file

**Free tier includes:**
- ⚡ Ultra-fast inference with Llama 3.3 70B
- 🎯 Generous rate limits (plenty for job hunting)
- 💳 No credit card required
- 🆓 Completely free to use

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
