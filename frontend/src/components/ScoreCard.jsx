const CARD_CONFIG = {
  problem:   { label: "Problem",    icon: "🎯", bg: "#FFF7ED" },
  market:    { label: "Market",     icon: "📊", bg: "#EFF6FF" },
  business:  { label: "Business",   icon: "💼", bg: "#F0FDF4" },
  technical: { label: "Technical",  icon: "⚙️",  bg: "#FAF5FF" },
  risk:      { label: "Risk",       icon: "🛡️",  bg: "#FFF1F2" },
};

function getScoreClass(score) {
  if (score >= 75) return "high";
  if (score >= 50) return "mid";
  return "low";
}

function ScoreCard({ category, data }) {
  const config = CARD_CONFIG[category] || { label: category, icon: "●", bg: "#F9FAFB" };
  const scoreClass = getScoreClass(data?.score ?? 0);
  const score = data?.score ?? 0;
  const summary = data?.summary || "";
  const strengths = data?.strengths || [];
  const weaknesses = data?.weaknesses || [];

  return (
    <div className={`eval-card card-${scoreClass}`}>
      <div className="eval-card-header">
        <div className="eval-card-title">
          <div className="eval-card-icon" style={{ background: config.bg }}>
            {config.icon}
          </div>
          {config.label}
        </div>
        <div className={`score-badge score-${scoreClass}`}>{score}</div>
      </div>

      <div className="score-bar-track">
        <div
          className={`score-bar-fill fill-${scoreClass}`}
          style={{ width: `${score}%` }}
        />
      </div>

      {summary && <p className="eval-summary">{summary}</p>}

      {(strengths.length > 0 || weaknesses.length > 0) && (
        <div className="eval-lists">
          <div className="eval-list strengths">
            <h5>Strengths</h5>
            <ul>
              {strengths.slice(0, 3).map((s, i) => <li key={i}>{s}</li>)}
            </ul>
          </div>
          <div className="eval-list weaknesses">
            <h5>Weaknesses</h5>
            <ul>
              {weaknesses.slice(0, 3).map((w, i) => <li key={i}>{w}</li>)}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default ScoreCard;