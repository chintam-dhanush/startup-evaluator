from agents.market_agent import evaluate_market

startup = {
    "startup_name": "FarmAI",
    "problem": "Farmers cannot identify crop diseases early.",
    "solution": "AI mobile app using leaf images."
}

result = evaluate_market(startup)

print(result)