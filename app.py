#!/usr/bin/env python3
"""
JobApply Web UI - Flask application
Run this for a browser-based interface
"""

from flask import Flask, render_template, request, jsonify, send_file
from pathlib import Path
import os
from datetime import datetime
from config import Config
from scraper import JobScraper
from llm_generator import ResponseGenerator

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize services
try:
    Config.validate()
    scraper = JobScraper()
    generator = ResponseGenerator()
except Exception as e:
    print(f"Configuration Error: {e}")
    print("Please set up your .env file first by running: python3 setup.py")
    exit(1)


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/scrape', methods=['POST'])
def scrape():
    """Scrape job posting from URL"""
    data = request.json
    url = data.get('url', '').strip()

    if not url:
        return jsonify({'error': 'Please provide a job URL'}), 400

    try:
        job_data = scraper.scrape(url)
        return jsonify({
            'success': True,
            'data': job_data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/generate', methods=['POST'])
def generate():
    """Generate application materials"""
    data = request.json

    job_title = data.get('job_title', '')
    company = data.get('company', '')
    description = data.get('description', '')
    output_types = data.get('output_types', [])

    if not all([job_title, company, description]):
        return jsonify({'error': 'Missing required fields'}), 400

    if not output_types:
        return jsonify({'error': 'Select at least one output type'}), 400

    try:
        resume = Config.load_resume()
        results = {}

        # Generate requested outputs
        if 'cover_letter' in output_types:
            results['cover_letter'] = generator.generate_cover_letter(
                job_title, company, description, resume
            )

        if 'application_email' in output_types:
            results['application_email'] = generator.generate_email(
                job_title, company, description, resume, email_type='application'
            )

        if 'recruiter_email' in output_types:
            results['recruiter_email'] = generator.generate_email(
                job_title, company, description, resume, email_type='recruiter'
            )

        if 'linkedin_message' in output_types:
            results['linkedin_message'] = generator.generate_linkedin_message(
                job_title, company, description, resume
            )

        # Save all outputs to files
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        saved_files = []

        for output_type, content in results.items():
            filename = save_output(job_title, company, content, output_type, timestamp)
            saved_files.append(filename)

        return jsonify({
            'success': True,
            'results': results,
            'saved_files': saved_files
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


def save_output(job_title: str, company: str, content: str, output_type: str, timestamp: str):
    """Save generated content to file"""
    safe_title = "".join(c for c in job_title if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_company = "".join(c for c in company if c.isalnum() or c in (' ', '-', '_')).strip()

    filename = f"{timestamp}_{safe_company}_{safe_title}_{output_type}.txt"
    filepath = Config.OUTPUT_DIR / filename

    filepath.write_text(content, encoding='utf-8')
    return str(filepath)


@app.route('/config')
def get_config():
    """Get configuration info"""
    return jsonify({
        'your_name': Config.YOUR_NAME,
        'your_email': Config.YOUR_EMAIL,
        'has_resume': len(Config.load_resume()) > 0
    })


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 JobApply Web UI Starting...")
    print("="*60)
    print(f"\n✓ Configuration loaded")
    print(f"✓ Your name: {Config.YOUR_NAME}")
    print(f"✓ Your email: {Config.YOUR_EMAIL}")
    print(f"✓ Resume: {'Loaded' if len(Config.load_resume()) > 0 else 'Not found - add to resume.txt'}")
    print(f"\n🌐 Open your browser to: http://localhost:5000")
    print("Press Ctrl+C to stop the server\n")
    print("="*60 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
