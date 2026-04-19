from pydantic import BaseModel, Field
from typing import List, Dict

class ResumeSkills(BaseModel):
    skills: List[str] = Field(..., description='List of skills extracted from the resume')
    skill_levels: Dict[str, str] = Field(...,description='Dictionary mapping each skill to its proficiency level: beginner, intermediate, advanced')