from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Resume(BaseModel):
    name: str
    email: str
    phone: str
    education: str
    skills: str


@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/generate")
def generate(data: Resume):

    resume = f"""
====================================
{data.name.upper()}
====================================

Email : {data.email}
Phone : {data.phone}

------------------------------------
EDUCATION
------------------------------------

{data.education}

------------------------------------
SKILLS
------------------------------------

{data.skills}

------------------------------------
PROFESSIONAL SUMMARY
------------------------------------

{data.name} is a motivated student with
a strong interest in technology,
continuous learning and innovation.

====================================
"""

    return {
        "response": resume
    }