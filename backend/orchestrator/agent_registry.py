from agents.problem_agent import evaluate_problem
from agents.market_agent import evaluate_market
from agents.business_agent import evaluate_business
from agents.technical_agent import evaluate_technical
from agents.risk_agent import evaluate_risk

AGENTS = [
    ("problem", evaluate_problem),
    ("market", evaluate_market),
    ("business", evaluate_business),
    ("technical", evaluate_technical),
    ("risk", evaluate_risk),
]