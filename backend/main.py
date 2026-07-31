from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from orchestrator.orchestrator import evaluate_startup
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from services.llm.groq_service import LLMResponseParsingError
import groq
import logging
from rag.setup import ensure_database

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("backend")

app = FastAPI(
    title="AI Startup Innovation Evaluation Platform",
    description="Multi-Agent AI Startup Evaluation System",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(groq.AuthenticationError)
async def groq_auth_exception_handler(request: Request, exc: groq.AuthenticationError):
    logger.error(f"Groq auth error: {exc}")
    return JSONResponse(
        status_code=401,
        content={"message": "Invalid or missing Groq API Key. Please configure your .env file.", "error_type": "AuthenticationError"}
    )

@app.exception_handler(groq.RateLimitError)
async def groq_rate_limit_exception_handler(request: Request, exc: groq.RateLimitError):
    logger.error(f"Groq rate limit: {exc}")
    return JSONResponse(
        status_code=429,
        content={"message": "Groq API rate limit reached. Please wait a moment and try again.", "error_type": "RateLimitError"}
    )

@app.exception_handler(groq.APITimeoutError)
async def groq_timeout_exception_handler(request: Request, exc: groq.APITimeoutError):
    logger.error(f"Groq API timeout: {exc}")
    return JSONResponse(
        status_code=504,
        content={"message": "Groq API request timed out. Please try again.", "error_type": "TimeoutError"}
    )

@app.exception_handler(groq.APIStatusError)
async def groq_api_status_exception_handler(request: Request, exc: groq.APIStatusError):
    logger.error(f"Groq API status error ({exc.status_code}): {exc.message}")
    return JSONResponse(
        status_code=exc.status_code if exc.status_code in [400, 401, 403, 404, 429, 500, 502, 503, 504] else 502,
        content={"message": f"Groq API error: {exc.message}", "error_type": "APIStatusError"}
    )

@app.exception_handler(LLMResponseParsingError)
async def llm_parsing_exception_handler(request: Request, exc: LLMResponseParsingError):
    logger.error(f"LLM Response parsing error: {exc}")
    return JSONResponse(
        status_code=502,
        content={"message": str(exc), "error_type": "LLMResponseParsingError"}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled server error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"message": f"An unexpected server error occurred: {str(exc)}", "error_type": "InternalServerError"}
    )

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Startup Evaluator!",
        "status": "Backend Running"
    }


class StartupInput(BaseModel):
    startup_name: str
    problem: str
    solution: str
    industry: str
    business_model: str
    target_customers: str
    stage: str


@app.post("/evaluate")
def evaluate(data: StartupInput):
    ensure_database()
    report = evaluate_startup(data.dict())
    return report