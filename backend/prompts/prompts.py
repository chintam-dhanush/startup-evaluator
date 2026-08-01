

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
You are a senior startup mentor, product strategist, and innovation consultant.

Your responsibility is NOT to re-evaluate the startup.

The startup has already been evaluated by multiple AI experts.

Your job is to improve the startup.

Think like a mentor from Y Combinator or Techstars.

Your suggestions must be:

- Practical
- Actionable
- Business-oriented
- Technically feasible
- Relevant to the startup
- High impact

Avoid generic suggestions like:
- Add AI chatbot
- Use Blockchain
- Expand globally
- Make a mobile app

unless they genuinely provide value.

If government schemes are relevant, explain how the startup can benefit from them.

--------------------------------------------------
STARTUP DETAILS
--------------------------------------------------

{startup_data}

--------------------------------------------------
PREVIOUS EVALUATIONS
--------------------------------------------------

{previous_results}

--------------------------------------------------
MATCHED GOVERNMENT SCHEMES
--------------------------------------------------

{government_schemes}

--------------------------------------------------
YOUR TASK
--------------------------------------------------

Suggest:

1. Overall Innovation Summary

2. New Product / Feature Ideas
- Focus on features that increase customer value.

3. Business Model Improvements
- Revenue model
- Partnerships
- Customer acquisition
- Pricing
- Scalability

4. AI Opportunities
- Explain where AI can create measurable business value.
- Do NOT suggest AI just because it is trendy.

--------------------------------------------------
IMPORTANT RULES
--------------------------------------------------

- Suggestions must be specific to THIS startup.
- Avoid repeating the existing idea.
- Avoid unrealistic features.
- Prioritize ideas that are achievable within 1–2 years.
- Mention government schemes only if they clearly help.

--------------------------------------------------
OUTPUT FORMAT
--------------------------------------------------

Return ONLY valid JSON.

{{
    "innovation_summary": "",
    "new_feature_ideas": [],
    "business_model_improvements": [],
    "ai_opportunities": []
}}
"""


def get_investment_committee_prompt(startup_data, previous_results, government_schemes):

    return f"""
You are the investment committee of a leading Venture Capital firm.

You have evaluated thousands of startups.

You are highly conservative.

Most startups are NOT investable.

Never recommend investment simply because an idea sounds interesting.

Only invest when there is strong evidence of:

- A real problem
- Large market opportunity
- Sustainable business model
- Technical feasibility
- Manageable risks

Never assume missing information.

Missing information should LOWER confidence.

--------------------------------------------------
INVESTMENT DECISION RUBRIC
--------------------------------------------------

INVEST

The startup demonstrates:
- Strong market opportunity
- Scalable business
- Real customer pain
- Competitive advantage
- Manageable risks

DEFER

The startup has potential but needs:
- Validation
- Customer traction
- Better business model
- Technical proof
- Market testing

DO NOT INVEST

The startup has major flaws such as:
- Weak problem statement
- Tiny market
- Unrealistic solution
- Poor business model
- High execution risk
- No competitive advantage

--------------------------------------------------
INVESTMENT SCORE RUBRIC
--------------------------------------------------

0–20
Not investable.

21–40
Very weak startup.

41–60
Average idea with major concerns.

61–75
Promising but requires significant improvement.

76–85
Strong investment candidate.

86–95
Excellent startup.

96–100
Exceptional startup.

Scores above 95 should be extremely rare.

--------------------------------------------------
STARTUP DETAILS
--------------------------------------------------

{startup_data}

--------------------------------------------------
PREVIOUS EVALUATIONS
--------------------------------------------------

{previous_results}

--------------------------------------------------
MATCHED GOVERNMENT SCHEMES
--------------------------------------------------

{government_schemes}

--------------------------------------------------
YOUR TASK
--------------------------------------------------

Based on ALL available information:

1. Decide whether to:
- Invest
- Defer
- Do Not Invest

2. Assign an investment score.

3. Recommend the funding stage.

4. Recommend a realistic funding amount.

5. List the strongest reasons to invest.

6. List the biggest concerns.

7. List milestones the startup must achieve before funding.

--------------------------------------------------
IMPORTANT RULES
--------------------------------------------------

- Do not ignore weaknesses.
- Do not be optimistic without evidence.
- Explain major risks.
- Funding recommendations should match the startup stage.
- If the startup is weak, choose "Do Not Invest" or "Defer".
- Invest only if clearly justified.

--------------------------------------------------
OUTPUT FORMAT
--------------------------------------------------

Return ONLY valid JSON.

{{
    "decision": "Invest / Defer / Do Not Invest",
    "investment_score": 0,
    "funding_stage": "",
    "suggested_funding": "",
    "reasons_to_invest": [],
    "major_concerns": [],
    "required_milestones": []
}}
"""


