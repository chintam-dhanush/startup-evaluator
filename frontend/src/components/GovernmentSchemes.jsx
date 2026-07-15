function GovernmentSchemes({ schemes }) {
  if (!schemes) return null;

  if (schemes.length === 0) {
    return (
      <div className="schemes-section">
        <p className="section-heading">Matched Government Schemes</p>
        <div className="empty-state">
          <div style={{ fontSize: "2rem" }}>🗂️</div>
          <p>
            No government schemes matched your startup profile.<br />
            Try refining your industry description or problem statement.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="schemes-section">
      <p className="section-heading">Matched Government Schemes</p>
      <div className="schemes-grid">
        {schemes.map((scheme, idx) => (
          <div className="scheme-card" key={idx}>
            <div className="scheme-card-header">
              <div className="scheme-name">{scheme.scheme_name}</div>
              <div className="scheme-ministry-badge">
                {scheme.ministry?.length > 20
                  ? scheme.ministry.split(" ").slice(0, 2).join(" ")
                  : scheme.ministry}
              </div>
            </div>

            {scheme.description && (
              <p className="scheme-description">{scheme.description}</p>
            )}

            {scheme.benefits && (
              <div className="scheme-detail-row">
                <span className="scheme-detail-label">Benefits</span>
                <span className="scheme-detail-value">{scheme.benefits}</span>
              </div>
            )}

            {scheme.eligibility && (
              <div className="scheme-detail-row">
                <span className="scheme-detail-label">Eligibility</span>
                <span className="scheme-detail-value">{scheme.eligibility}</span>
              </div>
            )}

            {(scheme.sector?.length > 0 || scheme.stage?.length > 0) && (
              <div className="scheme-tags">
                {scheme.stage?.map((s) => (
                  <span key={s} className="scheme-tag">
                    {s}
                  </span>
                ))}
                {scheme.sector?.slice(0, 3).map((s) => (
                  <span key={s} className="scheme-tag">
                    {s}
                  </span>
                ))}
              </div>
            )}

            {scheme.application_link && (
              <a
                href={scheme.application_link}
                target="_blank"
                rel="noopener noreferrer"
                className="scheme-apply-btn"
              >
                Apply Now ↗
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default GovernmentSchemes;
