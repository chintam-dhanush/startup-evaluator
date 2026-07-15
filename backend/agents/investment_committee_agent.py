from services.llm.groq_service import ask_llm_json
from prompts.prompts import get_investment_committee_prompt


def evaluate_investment(startup_data, previous_results, government_schemes):

    prompt = get_investment_committee_prompt(
        startup_data,
        previous_results,
        government_schemes
    )

    return ask_llm_json(prompt)