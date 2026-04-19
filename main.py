from fastapi import FastAPI, UploadFile, File
from parser import extract_text_from_pdf
from extractor import extract_skills

app = FastAPI()
@app.post("/parse-resume")
async def parse_resume(file: UploadFile):
    contents = await file.read()
    text = extract_text_from_pdf(contents)
    skills = extract_skills(text)
    return skills


