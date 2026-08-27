from fastapi import APIRouter
from pydantic import BaseModel

from pipeline import run_research


router = APIRouter()


class ResearchRequest(BaseModel):
    topic: str


@router.post("/research")
def research(data: ResearchRequest):

    result = run_research(data.topic)

    return {
        "topic": data.topic,
        "report": result["report"],
        "feedback": result["feedback"]
    }