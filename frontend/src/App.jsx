import "./index.css";
import Home from "./pages/Home";

function App() {
  return (
    <div className="app-wrapper">
      <header className="page-header">
        <div className="page-header-inner">
          <div className="page-header-brand">
            <div className="page-header-brand-icon">⚡</div>
            <div>
              <h1>Vanguard</h1>
              <span>AI Startup Evaluator</span>
            </div>
          </div>
          <div className="page-header-badge">Multi-Agent · RAG · Groq LLM</div>
        </div>
      </header>

      <main className="page-main">
        <Home />
      </main>

      <footer className="page-footer">
        © 2025 Vanguard — AI Startup Evaluator · Built with FastAPI, React & Groq LLM
      </footer>
    </div>
  );
}

export default App;
