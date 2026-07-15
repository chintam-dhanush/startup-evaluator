from services.llm.groq_service import ask_llm_json


def evaluate_startup_once(startup_data):
    """
    Calls the Groq LLM with all startup data and returns a structured evaluation
    across five dimensions: problem, market, business, technical, and risk.
    Each dimension returns a standardized schema with score, summary, strengths, and weaknesses.
    """
    prompt = f"""
You are an expert startup evaluation committee.

Analyze this startup.

Startup Name:
{startup_data.get("startup_name", "")}

Problem:
{startup_data.get("problem", "")}

Solution:
{startup_data.get("solution", "")}

Industry:
{startup_data.get("industry", "")}

Business Model:
{startup_data.get("business_model", "")}

Target Customers:
{startup_data.get("target_customers", "")}

Stage:
{startup_data.get("stage", "")}

Return ONLY valid JSON with this exact structure, where all "score" fields must be integer scores between 0 and 100:

{{
    "problem": {{
        "score": 85,
        "summary": "",
        "strengths": [],
        "weaknesses": []
    }},
    "market": {{
        "score": 80,
        "summary": "",
        "strengths": [],
        "weaknesses": []
    }},
    "business": {{
        "score": 75,
        "summary": "",
        "strengths": [],
        "weaknesses": []
    }},
    "technical": {{
        "score": 90,
        "summary": "",
        "strengths": [],
        "weaknesses": []
    }},
    "risk": {{
        "score": 70,
        "summary": "",
        "strengths": [],
        "weaknesses": []
    }}
}}
"""

    return ask_llm_json(prompt)