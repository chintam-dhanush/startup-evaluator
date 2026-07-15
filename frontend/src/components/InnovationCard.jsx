function InnovationCard({ innovation }) {
  if (!innovation) return null;

  const summary       = innovation.innovation_summary || "";
  // Handle both old field names (new_features/business_improvements) and new names
  const features      = innovation.new_feature_ideas || innovation.new_features || [];
  const improvements  = innovation.business_model_improvements || innovation.business_improvements || [];
  const aiOpps        = innovation.ai_opportunities || [];

  return (
    <div className="innovation-card">
      <div className="innovation-card-header">
        <h3>Innovation & Growth Suggestions</h3>
        <p>AI-powered recommendations to accelerate your startup's potential</p>
      </div>

      {summary && (
        <div className="innovation-summary">{summary}</div>
      )}

      <div className="innovation-body">
        {features.length > 0 && (
          <div className="innovation-section">
            <h5>New Feature Ideas</h5>
            <ul>
              {features.map((f, i) => <li key={i}>{f}</li>)}
            </ul>
          </div>
        )}

        {improvements.length > 0 && (
          <div className="innovation-section">
            <h5>Business Model Improvements</h5>
            <ul>
              {improvements.map((imp, i) => <li key={i}>{imp}</li>)}
            </ul>
          </div>
        )}

        {aiOpps.length > 0 && (
          <div className="innovation-section">
            <h5>AI Opportunities</h5>
            <ul>
              {aiOpps.map((opp, i) => <li key={i}>{opp}</li>)}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}

export default InnovationCard;