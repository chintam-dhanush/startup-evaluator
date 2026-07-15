from orchestrator.agent_registry import AGENTS
from agents.report_agent import generate_report
from agents.innovation_agent import evaluate_innovation
from agents.investment_committee_agent import evaluate_investment
from services.evaluation_service import evaluate_startup_once
from rag.retrieve import retrieve_schemes

def evaluate_startup(startup_data):

    # 1. Evaluate the startup on problem, market, business, technical, risk dimensions
    evaluation = evaluate_startup_once(startup_data)

    report = {}
    for agent_name, agent_function in AGENTS:
        report[agent_name] = agent_function(evaluation)

    # 2. Build focused retrieval query from problem, industry, target_customers, business_model/stage
    focused_query = (
        f"Industry: {startup_data.get('industry', '')}. "
        f"Problem: {startup_data.get('problem', '')}. "
        f"Target Customers: {startup_data.get('target_customers', '')}. "
        f"Stage: {startup_data.get('stage', '')}."
    )
    
    # 3. Retrieve matching government schemes
    government_schemes = retrieve_schemes(focused_query, top_k=3)

    # 4. Pass evaluation results & matching schemes to Innovation and Investment agents
    innovation = evaluate_innovation(
        startup_data,
        report,
        government_schemes
    )

    investment = evaluate_investment(
        startup_data,
        report,
        government_schemes
    )

    # 5. Assemble and score the final standardized report
    final_report = {
        "startup_name": startup_data.get("startup_name", "Unnamed Startup"),
        "overall_score": 0,
        "final_verdict": "",
        "evaluation": {
            "problem": report["problem"],
            "market": report["market"],
            "business": report["business"],
            "technical": report["technical"],
            "risk": report["risk"]
        },
        "innovation": innovation,
        "investment": investment,
        "government_schemes": government_schemes
    }

    final_report = generate_report(final_report)    

    return final_report