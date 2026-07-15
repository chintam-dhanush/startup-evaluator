function getDecisionClass(decision) {
  const d = (decision || "").toLowerCase();
  if (d.includes("invest") && !d.includes("not") && !d.includes("no")) return "invest";
  if (d.includes("defer")) return "defer";
  return "no";
}

function InvestmentCard({ investment }) {
  if (!investment) return null;

  const decision     = investment.decision || investment.investment_decision || "—";
  const score        = investment.investment_score ?? "—";
  const fundingStage = investment.funding_stage || "—";
  const funding      = investment.suggested_funding || "—";
  const reasons      = investment.reasons_to_invest || [];
  const concerns     = investment.major_concerns || [];
  const milestones   = investment.required_milestones || [];
  const decClass     = getDecisionClass(decision);

  return (
    <div className="investment-card">
      <div className="investment-card-header">
        <h3>Investment Committee</h3>
        <div className={`investment-decision-badge decision-${decClass}`}>{decision}</div>
      </div>

      <div className="investment-card-body">
        <div className="investment-meta-grid">
          <div className="investment-meta-item">
            <div className="investment-meta-label">Investment Score</div>
            <div className="investment-meta-value">{score} / 100</div>
          </div>
          <div className="investment-meta-item">
            <div className="investment-meta-label">Funding Stage</div>
            <div className="investment-meta-value">{fundingStage}</div>
          </div>
          <div className="investment-meta-item">
            <div className="investment-meta-label">Suggested Funding</div>
            <div className="investment-meta-value">{funding}</div>
          </div>
        </div>

        <div className="investment-details-grid">
          {reasons.length > 0 && (
            <div className="investment-detail invest-reasons">
              <h5>Reasons to Invest</h5>
              <ul>
                {reasons.map((r, i) => <li key={i}>{r}</li>)}
              </ul>
            </div>
          )}

          {concerns.length > 0 && (
            <div className="investment-detail invest-concerns">
              <h5>Major Concerns</h5>
              <ul>
                {concerns.map((c, i) => <li key={i}>{c}</li>)}
              </ul>
            </div>
          )}

          {milestones.length > 0 && (
            <div className="investment-detail invest-milestones">
              <h5>Required Milestones Before Funding</h5>
              <ul>
                {milestones.map((m, i) => <li key={i}>{m}</li>)}
              </ul>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default InvestmentCard;