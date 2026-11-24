# SmartMatch AI – Automated Resume & Job Description Analyzer

SmartMatch AI is a full-stack web application designed to help job seekers and students optimize their resumes for Applicant Tracking Systems (ATS). Users upload a PDF resume and paste a target job description to receive an instant compatibility score, missing skill tags, and AI-rewritten bullet points.

## 🚀 Key Features
* **Automated PDF Parsing:** Extracts raw text cleanly from uploaded PDF resumes using `pypdf`.
* **AI-Powered ATS Scoring:** Uses the Google Gemini API (`gemini-2.5-flash`) with structured JSON outputs to compare resume experience against job requirements.
* **Actionable Keyword Gap Analysis:** Identifies missing technical skills and tools required by the recruiter.
* **Bullet-Point Optimizer:** Generates 3 tailored, impact-driven resume bullet points aligned with the target role.

## 🛠️ Tech Stack
* **Backend:** Python, Flask, Gunicorn
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)
* **AI & Parsing:** Google Gemini GenAI SDK, PyPDF

## 📂 Project Structure
```text
smartmatch-ai/
├── app.py               # Flask backend & Gemini API integration
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Responsive frontend interface
└── README.md            # Project documentation
```

## ⚙️ How It Works
1. The user uploads a resume (`.pdf`) and enters a job description on the web interface.
2. Flask processes the multipart form data and extracts text from each page of the PDF.
3. The backend sends a structured prompt to the Gemini API requesting a match percentage, missing keywords, and improved bullet points.
4. The frontend dynamically renders the JSON response into an interactive report.
