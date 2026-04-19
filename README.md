# Tantomi Resume Parser API

An AI-powered REST API that extracts technical skills and proficiency levels
from uploaded resume PDFs, built as the backend service for the Tantomi
skill progress tracking application.

## Overview

This API provides an end-to-end resume parsing pipeline for:

* **File Handling:** Accepts PDF resume uploads via a REST endpoint using FastAPI.
* **Text Extraction:** Parses raw text from PDF files using PyMuPDF.
* **Skill Extraction:** Uses LangChain and GPT-4o-mini to identify technical
  skills and assess proficiency levels from extracted resume text.
* **Structured Output:** Returns validated, structured JSON via Pydantic schemas
  ready for direct insertion into the Tantomi Supabase database.

## Technical Stack

* **Language:** Python 3.12
* **Framework:** FastAPI
* **AI / LLM:** LangChain, OpenAI GPT-4o-mini
* **PDF Parsing:** PyMuPDF (fitz)
* **Data Validation:** Pydantic v2
* **Environment:** Uvicorn, python-dotenv

## Project Structure

| File | Responsibility |
|------|---------------|
| `main.py` | FastAPI routes |
| `parser.py` | PDF text extraction |
| `extractor.py` | LangChain skill extraction |
| `models.py` | Pydantic schemas |
| `.env.example` | Environment variable template |
| `requirements.txt` | Dependencies |

## API Endpoints

* **POST /parse-resume** — Accepts a PDF file upload, extracts text, and returns
  a structured list of technical skills and proficiency levels.

### Example Response

```json
{
  "skills": ["Python", "scikit-learn", "SQL", "React", "Firebase"],
  "skill_levels": {
    "Python": "some experience",
    "scikit-learn": "some experience",
    "SQL": "beginner",
    "React": "beginner",
    "Firebase": "beginner"
  }
}
```

## Execution Instructions

1. Clone the repository and navigate to the project folder.
2. Create and activate a virtual environment: `python -m venv venv` then `.\venv\Scripts\Activate.ps1`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your OpenAI API key: `OPENAI_API_KEY=your_openai_key_here`
5. Start the server: `uvicorn main:app --reload`
6. Visit `http://localhost:8000/docs` to access the interactive API documentation.

---

**Author:** Verah Dulay
**Date:** April 2026
