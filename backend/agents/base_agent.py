from services.llm.groq_service import ask_llm_json


def execute_agent(prompt_function, startup_data):
    """
    Generic function to execute any AI agent.

    Parameters:
        prompt_function : Function that generates the prompt
        startup_data    : Dictionary containing startup details

    Returns:
        Parsed JSON response from the LLM.
    """

    prompt = prompt_function(startup_data)

    result = ask_llm_json(prompt)

    return result