
from agents.problem_agent import evaluate_problem

startup = {
    "startup_name": "FarmAI",
    "problem": "Farmers cannot identify crop diseases early.",
    "solution": "An AI-powered mobile app that detects crop diseases from leaf images."
}

result = evaluate_problem(startup)

print(result)