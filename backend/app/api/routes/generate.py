
from fastapi import APIRouter
from app.schemas.generator import GenerateRequest
from app.services.generator_service import GeneratorService

router = APIRouter()

@router.post("/generate")
def generate(payload: GenerateRequest):
    return GeneratorService().generate(payload)
