import HeroCard from "./HeroCard";
import ScoreCard from "./ScoreCard";
import EvalChart from "./EvalChart";
import InvestmentCard from "./InvestmentCard";
import InnovationCard from "./InnovationCard";
import GovernmentSchemes from "./GovernmentSchemes";

function Dashboard({ result }) {
  if (!result) return null;

  const evaluation = result.evaluation || {};

  return (
    <div className="dashboard">
      {/* Section header */}
      <div className="dashboard-header">
        <h2>Evaluation Report</h2>
        <div className="dashboard-divider" />
      </div>

      {/* 1. Hero Card — Startup name, overall score, verdict */}
      <HeroCard
        startupName={result.startup_name}
        score={result.overall_score}
        verdict={result.final_verdict}
      />

      {/* 2. Radar Chart */}
      <EvalChart evaluation={evaluation} />

      {/* 3. Five Evaluation Dimension Cards */}
      <p className="section-heading" style={{ marginBottom: "1rem" }}>Evaluation Breakdown</p>
      <div className="eval-grid" style={{ marginBottom: "2rem" }}>
        {["problem", "market", "business", "technical", "risk"].map((cat) => (
          <ScoreCard key={cat} category={cat} data={evaluation[cat]} />
        ))}
      </div>

      {/* 4. Investment Committee */}
      <p className="section-heading" style={{ marginBottom: "1rem" }}>Investment Committee Decision</p>
      <InvestmentCard investment={result.investment} />

      {/* 5. Innovation Suggestions */}
      <p className="section-heading" style={{ marginBottom: "1rem" }}>Innovation & Growth</p>
      <InnovationCard innovation={result.innovation} />

      {/* 6. Government Schemes */}
      <GovernmentSchemes schemes={result.government_schemes || []} />
    </div>
  );
}

export default Dashboard;