import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re


class JobScraper:
    """Scrape job descriptions from various job posting URLs"""

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def scrape(self, url: str) -> dict:
        """
        Scrape job posting from URL

        Args:
            url: Job posting URL

        Returns:
            dict with keys: title, company, description, url
        """
        domain = urlparse(url).netloc

        # Route to specific scraper based on domain
        if 'linkedin.com' in domain:
            return self._scrape_linkedin(url)
        elif 'indeed.com' in domain:
            return self._scrape_indeed(url)
        elif 'greenhouse.io' in domain:
            return self._scrape_greenhouse(url)
        else:
            # Generic scraper for unknown sites
            return self._scrape_generic(url)

    def _scrape_generic(self, url: str) -> dict:
        """Generic scraper for any job posting page"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Try to extract text content
            # Remove script and style elements
            for script in soup(['script', 'style', 'nav', 'footer', 'header']):
                script.decompose()

            # Get text
            text = soup.get_text(separator='\n', strip=True)

            # Clean up multiple newlines
            text = re.sub(r'\n+', '\n', text)

            return {
                'title': soup.title.string if soup.title else "Unknown Position",
                'company': "Unknown Company",
                'description': text,
                'url': url
            }
        except Exception as e:
            return {
                'title': 'Error',
                'company': 'Error',
                'description': f'Failed to scrape: {str(e)}',
                'url': url
            }

    def _scrape_linkedin(self, url: str) -> dict:
        """Scrape LinkedIn job postings"""
        # LinkedIn often requires authentication, fallback to generic
        return self._scrape_generic(url)

    def _scrape_indeed(self, url: str) -> dict:
        """Scrape Indeed job postings"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Indeed-specific selectors (these may change)
            title = soup.find('h1', class_='jobsearch-JobInfoHeader-title')
            company = soup.find('div', {'data-company-name': True})
            description = soup.find('div', id='jobDescriptionText')

            return {
                'title': title.get_text(strip=True) if title else "Unknown Position",
                'company': company.get('data-company-name') if company else "Unknown Company",
                'description': description.get_text(separator='\n', strip=True) if description else "",
                'url': url
            }
        except Exception as e:
            return self._scrape_generic(url)

    def _scrape_greenhouse(self, url: str) -> dict:
        """Scrape Greenhouse job postings"""
        return self._scrape_generic(url)
