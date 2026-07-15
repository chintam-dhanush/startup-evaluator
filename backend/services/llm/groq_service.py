import re
import os
import json
import logging

from groq import Groq
from dotenv import load_dotenv

logger = logging.getLogger("backend.llm")

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")


def ask_llm(prompt: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content



class LLMResponseParsingError(Exception):
    """Custom exception raised when JSON parsing of LLM response fails after retry."""
    pass


def extract_json(text: str):
    text_stripped = text.strip()
    
    # 1. Try direct parse
    try:
        return json.loads(text_stripped)
    except json.JSONDecodeError:
        pass

    # 2. Try clean markdown code blocks
    clean_text = re.sub(r"^```json\s*", "", text_stripped, flags=re.IGNORECASE)
    clean_text = re.sub(r"^```\s*", "", clean_text)
    clean_text = re.sub(r"\s*```$", "", clean_text)
    
    try:
        return json.loads(clean_text.strip())
    except json.JSONDecodeError:
        pass

    # 3. Try to locate first '{' and last '}'
    first_brace = text.find("{")
    last_brace = text.rfind("}")
    if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
        candidate = text[first_brace:last_brace+1]
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            pass
            
    raise json.JSONDecodeError("Could not extract valid JSON from LLM response text.", text, 0)


def log_safe(message: str):
    safe = message.encode("ascii", errors="replace").decode("ascii")
    logger.info(safe)


def ask_llm_json(prompt: str):
    response = ask_llm(prompt)

    log_safe("RAW LLM RESPONSE:")
    log_safe(response)

    try:
        return extract_json(response)
    except Exception as e:
        logger.warning("Initial JSON parsing failed: %s. Retrying with stricter instructions.", e)

        retry_prompt = (
            prompt
            + "\n\nCRITICAL: Your previous response was not valid JSON. "
            "You MUST return ONLY the raw JSON object matching the requested schema. "
            "Do not include any explanation, intro text, markdown code blocks, or fences."
        )

        try:
            retry_response = ask_llm(retry_prompt)
            log_safe("RETRY RAW LLM RESPONSE:")
            log_safe(retry_response)
            return extract_json(retry_response)
        except Exception as retry_err:
            raise LLMResponseParsingError(
                f"Failed to parse structured JSON from LLM response after retry: {retry_err}"
            )