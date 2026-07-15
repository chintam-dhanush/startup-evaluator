import {
  RadarChart,
  Radar,
  PolarGrid,
  PolarAngleAxis,
  ResponsiveContainer,
  Tooltip,
} from "recharts";

function EvalChart({ evaluation }) {
  if (!evaluation) return null;

  const data = [
    { subject: "Problem",   score: evaluation.problem?.score   ?? 0 },
    { subject: "Market",    score: evaluation.market?.score    ?? 0 },
    { subject: "Business",  score: evaluation.business?.score  ?? 0 },
    { subject: "Technical", score: evaluation.technical?.score ?? 0 },
    { subject: "Risk",      score: evaluation.risk?.score      ?? 0 },
  ];

  const CustomTooltip = ({ active, payload }) => {
    if (active && payload && payload.length) {
      return (
        <div style={{
          background: "#fff",
          border: "1px solid #D1D5DB",
          borderRadius: "8px",
          padding: "8px 14px",
          fontSize: "0.85rem",
          fontFamily: "Plus Jakarta Sans, sans-serif",
          boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
        }}>
          <strong>{payload[0].payload.subject}</strong>
          <div style={{ color: "#0D7F6E", fontWeight: 700 }}>
            Score: {payload[0].value}
          </div>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="chart-card">
      <p className="section-heading">Dimension Radar</p>
      <ResponsiveContainer width="100%" height={320}>
        <RadarChart cx="50%" cy="50%" outerRadius="70%" data={data}>
          <PolarGrid stroke="#E5E7EB" />
          <PolarAngleAxis
            dataKey="subject"
            tick={{
              fill: "#374151",
              fontSize: 13,
              fontFamily: "Plus Jakarta Sans, sans-serif",
              fontWeight: 600,
            }}
          />
          <Radar
            name="Score"
            dataKey="score"
            stroke="#0D7F6E"
            fill="#0D7F6E"
            fillOpacity={0.18}
            strokeWidth={2}
          />
          <Tooltip content={<CustomTooltip />} />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default EvalChart;
