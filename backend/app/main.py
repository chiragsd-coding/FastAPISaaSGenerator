
from fastapi import FastAPI
from app.api.routes.generate import router as generate_router

app = FastAPI(title="Boilerplate Generator")
app.include_router(generate_router,prefix="/api/v1")

@app.get("/health")
def health():
    return {"status":"ok"}
