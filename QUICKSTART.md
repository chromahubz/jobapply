# 🚀 Quick Start Guide

## The Absolute Easiest Way to Get Started

### 1️⃣ Choose Your Interface

**🎨 Web UI (Recommended - Beautiful Apple Design)**

**Linux/Mac:**
```bash
./run_web.sh
```

**Windows:**
```bash
run_web.bat
```

Opens in your browser at http://localhost:5000

**OR**

**💻 Command Line (For Terminal Fans)**

**Linux/Mac:**
```bash
./run.sh
```

**Windows:**
```bash
run.bat
```

Both scripts will:
- Check if you need setup
- Install everything automatically
- Guide you through configuration
- Launch the app

### 2️⃣ Get Your Free Groq API Key (2 Minutes)

While the setup runs, open your browser:

1. Go to: **https://console.groq.com/keys**
2. Sign up with your email (no credit card needed!)
3. Click "Create API Key"
4. Copy the key
5. Paste it when the setup asks

**That's literally it!** 🎉

---

## What Happens Next?

The setup will ask you:
- ✅ Your Groq API key
- ✅ Your name
- ✅ Your email
- ✅ Your phone (optional)
- ✅ Your LinkedIn (optional)
- ✅ If you want to paste your resume now

Then you're done!

---

## Using the App

Once setup is complete:

1. **Run the app:**
   ```bash
   python main.py
   ```
   (Or just run `./run.sh` again)

2. **Paste a job URL** when prompted
   - LinkedIn job posting
   - Indeed listing
   - Any job board URL

3. **Choose what to generate:**
   - Cover letter
   - Application email
   - Recruiter outreach email
   - LinkedIn message
   - All of the above! (recommended)

4. **Find your files** in the `./applications/` folder

---

## Example Workflow

```
$ python main.py

Enter job URL: https://www.linkedin.com/jobs/view/123456

✓ Scraped: Software Engineer at Google

Choose what to generate:
  1. Cover letter
  2. Application email
  3. Recruiter outreach email
  4. LinkedIn message
  5. All of the above

Choice: 5

✓ Generated cover letter
✓ Generated application email
✓ Generated recruiter email
✓ Generated LinkedIn message

Saved to: ./applications/20260121_143022_Google_Software_Engineer_*
```

---

## Troubleshooting

**"Module not found" error?**
```bash
pip install -r requirements.txt
```

**"GROQ_API_KEY is required" error?**
- Get your key at https://console.groq.com/keys
- Add it to `.env` file

**Scraping not working?**
- Try manually pasting the job description
- The app will prompt you if scraping fails

---

## Tips for Best Results

💡 **Resume Quality**: The better your resume, the better AI outputs
💡 **Job Descriptions**: More detailed = better tailored responses
💡 **Review & Edit**: Always review AI content before sending
💡 **Batch Process**: Generate all formats, pick the best one
💡 **Update Resume**: Keep resume.txt current with your latest experience

---

## Need Help?

- 📖 Read the full [README.md](README.md)
- 🐛 Report issues on GitHub
- 💬 Check out the code - it's all documented!

**Happy job hunting!** 🎯
