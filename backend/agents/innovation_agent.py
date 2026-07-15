from services.llm.groq_service import ask_llm_json
from prompts.prompts import get_innovation_prompt


def evaluate_innovation(startup_data, previous_results, government_schemes):

    prompt = get_innovation_prompt(
        startup_data,
        previous_results,
        government_schemes
    )

    return ask_llm_json(prompt)