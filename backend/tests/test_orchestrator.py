from orchestrator.orchestrator import evaluate_startup

startup = {
    "startup_name": "FarmAI",
    "problem": "Farmers cannot identify crop diseases early.",
    "solution": "An AI-powered app detects diseases using leaf images.",
    "industry": "Agriculture",
    "business_model": "B2B SaaS subscription for agro-cooperatives",
    "target_customers": "Small and medium-scale farmers",
    "stage": "Prototype"
}

report = evaluate_startup(startup)

import json
try:
    print(json.dumps(report, indent=2))
except UnicodeEncodeError:
    print(json.dumps(report, indent=2).encode('ascii', errors='replace').decode('ascii'))