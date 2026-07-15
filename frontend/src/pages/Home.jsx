import { useState } from "react";
import StartupForm from "../components/StartupForm";
import Dashboard from "../components/Dashboard";

function Home() {
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleResult = (data) => {
    setError(null);
    setResult(data);
    // Scroll to dashboard
    setTimeout(() => {
      document.getElementById("results-section")?.scrollIntoView({ behavior: "smooth" });
    }, 100);
  };

  const handleError = (errMsg) => {
    setResult(null);
    setError(errMsg);
  };

  return (
    <>
      <StartupForm onResult={handleResult} onError={handleError} />

      {error && (
        <div className="error-card" style={{ marginTop: "2rem" }}>
          <div className="error-card-icon">⚠️</div>
          <div>
            <h4>Evaluation Failed</h4>
            <p>{error}</p>
          </div>
        </div>
      )}

      {result && (
        <div id="results-section" style={{ marginTop: "3rem" }}>
          <Dashboard result={result} />
        </div>
      )}
    </>
  );
}

export default Home;