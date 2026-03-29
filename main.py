from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

app = FastAPI()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event("startup")
def startup():
    logger.info("Zakeus System started")

# Root
@app.get("/")
def root():
    return {
        "message": "Zakeus System API aktif",
        "status": "running"
    }

# Health Check
@app.get("/health")
def health():
    return {"status": "ok"}

# Info
@app.get("/info")
def info():
    return {
        "system": "Zakeus",
        "version": "1.0",
        "status": "stable"
    }

# Global Error Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Terjadi error, tapi sistem tetap stabil"}
    )