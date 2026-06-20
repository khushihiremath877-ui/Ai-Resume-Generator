from fastapi import APIRouter

from app.schemas.resume_schema import Resume
from app.services.resume_service import generate_resume

router = APIRouter()

@router.post("/generate")
def generate(data: Resume):

    resume = generate_resume(data)

    return {
        "response": resume
    }