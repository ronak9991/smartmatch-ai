import os
import json
from flask import Flask, render_template, request, jsonify
from pypdf import PdfReader
from google import genai
from google.genai import types

app = Flask(__name__)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files or "jd" not in request.form:
        return jsonify({"error": "Please upload a resume PDF and enter a job description."}), 400

    resume_file = request.files["resume"]
    jd_text = request.form["jd"]

    if resume_file.filename == "" or not jd_text.strip():
        return jsonify({"error": "Both resume file and job description are required."}), 400

    try:
        resume_text = extract_text_from_pdf(resume_file)
        prompt = f"""
        You are an expert ATS and technical recruiter. Compare the Resume against the Job Description.
        Return ONLY a valid JSON object with these exact keys:
        - "match_score": integer from 0 to 100
        - "missing_keywords": list of strings
        - "improved_bullets": list of 3 strings (rewritten resume bullet points tailored to this JD)
        - "summary": 2-sentence constructive feedback

        Resume: {resume_text}
        Job Description: {jd_text}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(response_mime_type="application/json")
        )
        return jsonify(json.loads(response.text))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
