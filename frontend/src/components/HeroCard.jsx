function getVerdictClass(verdict) {
  const v = (verdict || "").toLowerCase();
  if (v.includes("excellent")) return "excellent";
  if (v.includes("promising")) return "promising";
  if (v.includes("needs")) return "needs-work";
  return "high-risk";
}

function ScoreRing({ score }) {
  const radius = 52;
  const circumference = 2 * Math.PI * radius;
  const color = score >= 75 ? "#1A7A4A" : score >= 55 ? "#C9A84C" : "#9B1C1C";
  const offset = circumference - (score / 100) * circumference;

  return (
    <div className="hero-score-ring">
      <svg width="130" height="130" viewBox="0 0 130 130">
        {/* Track */}
        <circle
          cx="65" cy="65" r={radius}
          fill="none"
          stroke="rgba(255,255,255,0.1)"
          strokeWidth="8"
        />
        {/* Fill */}
        <circle
          cx="65" cy="65" r={radius}
          fill="none"
          stroke={color}
          strokeWidth="8"
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          style={{ transition: "stroke-dashoffset 1.2s cubic-bezier(0.34,1.56,0.64,1)" }}
        />
      </svg>
      <div style={{ textAlign: "center" }}>
        <div className="hero-score-value">{score}</div>
        <div className="hero-score-label">/ 100</div>
      </div>
    </div>
  );
}

function HeroCard({ startupName, score, verdict }) {
  const verdictClass = getVerdictClass(verdict);

  return (
    <div className="hero-card">
      <div>
        <div className="hero-startup-label">Startup Evaluation Report</div>
        <div className="hero-startup-name">{startupName || "Your Startup"}</div>
        <div className={`hero-verdict ${verdictClass}`}>
          {verdictClass === "excellent" && "★ "}
          {verdictClass === "promising" && "▲ "}
          {verdictClass === "needs-work" && "⚠ "}
          {verdictClass === "high-risk" && "⚡ "}
          {verdict}
        </div>
      </div>
      <ScoreRing score={score} />
    </div>
  );
}

export default HeroCard;