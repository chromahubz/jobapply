from groq import Groq
from config import Config


class ResponseGenerator:
    """Generate optimized job application responses using Groq LLM"""

    def __init__(self):
        Config.validate()
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = Config.LLM_MODEL

    def generate_cover_letter(self, job_info: dict, resume_text: str) -> str:
        """
        Generate a tailored cover letter

        Args:
            job_info: Dict containing title, company, description, url
            resume_text: Your resume/CV text

        Returns:
            Generated cover letter text
        """
        prompt = f"""You are a professional career advisor helping write a compelling cover letter.

Job Title: {job_info['title']}
Company: {job_info['company']}

Job Description:
{job_info['description'][:3000]}

My Resume/Background:
{resume_text[:2000]}

Personal Info:
Name: {Config.YOUR_NAME}
Email: {Config.YOUR_EMAIL}
Phone: {Config.YOUR_PHONE}

Write a professional, compelling cover letter that:
1. Is addressed to the hiring manager (use "Dear Hiring Manager" if name unknown)
2. Shows genuine interest in this specific role and company
3. Highlights relevant experience from my resume that matches the job requirements
4. Is concise (3-4 paragraphs max)
5. Has a professional tone but sounds human and authentic
6. Includes a strong closing call-to-action

Do not use overly flowery language or clichés. Be specific about why I'm a good fit."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=Config.LLM_TEMPERATURE,
            max_tokens=Config.LLM_MAX_TOKENS
        )

        return response.choices[0].message.content

    def generate_email(self, job_info: dict, resume_text: str, email_type: str = "application") -> str:
        """
        Generate a professional email

        Args:
            job_info: Dict containing title, company, description, url
            resume_text: Your resume/CV text
            email_type: Type of email - "application", "recruiter", "follow_up"

        Returns:
            Generated email text with subject line
        """
        if email_type == "recruiter":
            context = "reaching out to a recruiter about this position"
        elif email_type == "follow_up":
            context = "following up on a previous application"
        else:
            context = "applying for this position"

        prompt = f"""You are writing a professional email {context}.

Job Title: {job_info['title']}
Company: {job_info['company']}

Job Description:
{job_info['description'][:2000]}

My Background:
{resume_text[:1500]}

Personal Info:
Name: {Config.YOUR_NAME}
Email: {Config.YOUR_EMAIL}

Write a professional email that:
1. Starts with a compelling subject line (on first line, prefixed with "Subject: ")
2. Has a brief, engaging opening
3. Clearly states my interest and relevant qualifications
4. Is concise (4-6 sentences in the body)
5. Includes a clear call-to-action
6. Ends with professional sign-off

Keep it brief and impactful. Recruiters are busy."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=Config.LLM_TEMPERATURE,
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_linkedin_message(self, job_info: dict, resume_text: str) -> str:
        """
        Generate a LinkedIn connection/InMail message

        Args:
            job_info: Dict containing title, company, description, url
            resume_text: Your resume/CV text

        Returns:
            Generated LinkedIn message (short)
        """
        prompt = f"""Write a brief LinkedIn message to a recruiter or hiring manager about this role.

Job Title: {job_info['title']}
Company: {job_info['company']}

My Background:
{resume_text[:1000]}

Requirements:
1. Maximum 300 characters (LinkedIn limit for connection requests) OR 2000 for InMail
2. Personalized and specific to the role
3. Shows clear value proposition
4. Friendly but professional tone
5. Includes a subtle call-to-action

Write ONLY the message text, no subject line needed."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=Config.LLM_TEMPERATURE,
            max_tokens=500
        )

        return response.choices[0].message.content
