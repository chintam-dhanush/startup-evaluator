def get_verdict(score):

    if score >= 85:
        return "Excellent Startup"

    elif score >= 70:
        return "Promising Startup"

    elif score >= 50:
        return "Needs Improvement"

    return "High Risk"


def generate_report(report):

    evaluation = report["evaluation"]
    scores = [
        evaluation["problem"]["score"],
        evaluation["market"]["score"],
        evaluation["business"]["score"],
        evaluation["technical"]["score"],
        evaluation["risk"]["score"],
    ]

    overall_score = round(sum(scores) / len(scores))

    report["overall_score"] = overall_score
    report["final_verdict"] = get_verdict(overall_score)

    return report