

def get_problem_prompt(startup_data):

    return f"""
You are an expert startup evaluator.

Your task is ONLY to evaluate the startup problem.

Startup Name:
{startup_data["startup_name"]}

Problem:
{startup_data["problem"]}

Solution:
{startup_data["solution"]}

Evaluate:

1. Is the problem real?
2. Is it significant?
3. Who experiences it?
4. Does the solution actually solve it?

Return ONLY JSON.

{{
"problem_score":0,
"problem_summary":"",
"strengths":[],
"weaknesses":[]
}}
"""


def get_market_prompt(startup_data):

    return f"""
You are a senior Venture Capital analyst.

Evaluate ONLY the market potential.

Startup Name:
{startup_data["startup_name"]}

Problem:
{startup_data["problem"]}

Solution:
{startup_data["solution"]}

Analyze:

1. Target customers
2. Market demand
3. Existing competitors
4. Growth potential
5. Entry barriers

Return ONLY JSON.

{{
"market_score":0,
"market_summary":"",
"target_customers":"",
"competitors":[],
"opportunities":[]
}}
"""


def get_business_prompt(startup_data):

    return f"""
You are a startup mentor and MBA graduate specializing in startup business models.

Evaluate ONLY the business model.

Startup Name:
{startup_data["startup_name"]}

Problem:
{startup_data["problem"]}

Solution:
{startup_data["solution"]}

Analyze:

1. Revenue Model
2. Monetization
3. Pricing Strategy
4. Scalability
5. Customer Acquisition

Return ONLY JSON.

{{
"business_score":0,
"business_summary":"",
"revenue_model":"",
"pricing_strategy":"",
"scalability":"",
"recommendations":[]
}}
"""


def get_technical_prompt(startup_data):

    return f"""
You are a Principal Software Engineer and AI Architect.

Evaluate ONLY the technical feasibility of this startup.

Startup Name:
{startup_data["startup_name"]}

Problem:
{startup_data["problem"]}

Solution:
{startup_data["solution"]}

Evaluate:

1. Technical feasibility
2. AI complexity
3. Development difficulty
4. Infrastructure requirements
5. Scalability of the technology

Return ONLY valid JSON.

{{
    "technical_score": 0,
    "technical_summary": "",
    "recommended_stack": [
        "..."
    ],
    "development_difficulty": "",
    "scalability": "",
    "recommendations": [
        "..."
    ]
}}
"""


def get_risk_prompt(startup_data):

    return f"""
You are an experienced startup risk consultant.

Evaluate ONLY the risks associated with this startup.

Startup Name:
{startup_data["startup_name"]}

Problem:
{startup_data["problem"]}

Solution:
{startup_data["solution"]}

Analyze:

1. Technical Risk
2. Financial Risk
3. Market Risk
4. Legal Risk
5. Operational Risk

Return ONLY valid JSON.

{{
    "risk_score": 0,
    "risk_summary": "",
    "technical_risk": "",
    "financial_risk": "",
    "market_risk": "",
    "legal_risk": "",
    "operational_risk": "",
    "mitigation": [
        "..."
    ]
}}
"""

def get_innovation_prompt(startup_data, previous_results, government_schemes):

    return f"""
You are an experienced startup mentor.

Below is a startup idea, evaluations from multiple expert AI agents, and a list of matched government schemes.

Startup:
{startup_data}

Previous Evaluations:
{previous_results}

Matched Government Schemes:
{government_schemes}

Your task is NOT to re-evaluate.
Instead, suggest creative improvements, leveraging the matched government schemes if applicable.

Suggest:
1. New Feature Ideas
2. Business Model Improvements
3. AI Opportunities

Return ONLY valid JSON matching this structure:
{{
    "innovation_summary": "Overall summary of the startup's innovation potential and suggestions.",
    "new_feature_ideas": [
        "Feature idea 1",
        "Feature idea 2"
    ],
    "business_model_improvements": [
        "Improvement 1",
        "Improvement 2"
    ],
    "ai_opportunities": [
        "AI Opportunity 1",
        "AI Opportunity 2"
    ]
}}
"""

def get_investment_committee_prompt(startup_data, previous_results, government_schemes):

    return f"""
You are an investment committee consisting of experienced Venture Capitalists.

Startup Details:
{startup_data}

Previous Evaluations:
{previous_results}

Matched Government Schemes:
{government_schemes}

Based on all the information, decide:
1. Investment Decision (e.g. Invest, Do Not Invest, Defer)
2. Investment Score (0-100)
3. Suggested Funding Stage
4. Suggested Funding Amount
5. Reasons to Invest
6. Major Concerns
7. Required Milestones before funding

Return ONLY valid JSON matching this structure:
{{
    "decision": "Invest / Do Not Invest / Defer",
    "investment_score": 85,
    "funding_stage": "Seed / Pre-Series A / etc.",
    "suggested_funding": "e.g. ₹50 Lakhs / $100K",
    "reasons_to_invest": [
        "Reason 1",
        "Reason 2"
    ],
    "major_concerns": [
        "Concern 1",
        "Concern 2"
    ],
    "required_milestones": [
        "Milestone 1",
        "Milestone 2"
    ]
}}
"""




