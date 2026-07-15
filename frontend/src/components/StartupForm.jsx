import { useState, useEffect } from "react";
import api from "../services/api";

const STAGES = ["Idea", "Prototype", "MVP", "Seed", "Pre-Series A", "Series A", "Growth", "Scale"];
const INDUSTRIES = [
  "Agriculture / Agri-Tech",
  "AI / Machine Learning",
  "Biotechnology / Healthcare",
  "Clean Energy / ClimaTech",
  "Cybersecurity",
  "E-Commerce / Retail",
  "Education / EdTech",
  "FinTech / Payments",
  "Food Processing",
  "IoT / Hardware",
  "Legal / LegalTech",
  "Logistics / Supply Chain",
  "Manufacturing",
  "Media / Entertainment",
  "Real Estate / PropTech",
  "SaaS / B2B Software",
  "Social Impact",
  "Telecommunications",
  "Other",
];

const LOADING_STEPS = [
  "Analyzing problem statement...",
  "Evaluating market potential...",
  "Assessing business model...",
  "Reviewing technical feasibility...",
  "Identifying risks...",
  "Retrieving government schemes...",
  "Generating investment recommendation...",
  "Synthesizing innovation insights...",
  "Compiling final report...",
];

const SAMPLE_DATA = {
  startup_name: "MediSense AI",
  problem:
    "Rural hospitals in India lack affordable diagnostic tools, leading to delayed treatment for common diseases like diabetes, hypertension, and anaemia.",
  solution:
    "An AI-powered handheld diagnostic device that uses computer vision and ML to screen for 10+ diseases from a single blood drop, costing 1/20th of conventional lab tests.",
  industry: "Biotechnology / Healthcare",
  business_model:
    "B2B2C — sell devices to primary health centres and rural clinics (B2B), and offer a per-test subscription for the AI cloud analysis service.",
  target_customers:
    "Government-run primary health centres (PHCs), private rural clinics, NGO health programmes, and ASHA workers in Tier-3 cities and villages.",
  stage: "Prototype",
};

const validate = (formData) => {
  const errors = {};
  if (!formData.startup_name.trim()) errors.startup_name = "Startup name is required.";
  if (!formData.problem.trim() || formData.problem.trim().length < 30)
    errors.problem = "Please describe the problem in at least 30 characters.";
  if (!formData.solution.trim() || formData.solution.trim().length < 30)
    errors.solution = "Please describe the solution in at least 30 characters.";
  if (!formData.industry) errors.industry = "Select an industry.";
  if (!formData.business_model.trim()) errors.business_model = "Describe your business model.";
  if (!formData.target_customers.trim()) errors.target_customers = "Describe your target customers.";
  if (!formData.stage) errors.stage = "Select a startup stage.";
  return errors;
};

function StartupForm({ onResult, onError }) {
  const [formData, setFormData] = useState({
    startup_name: "",
    problem: "",
    solution: "",
    industry: "",
    business_model: "",
    target_customers: "",
    stage: "",
  });

  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);
  const [doneSteps, setDoneSteps] = useState([]);

  // Cycle through loading steps during evaluation
  useEffect(() => {
    if (!loading) return;
    setCurrentStep(0);
    setDoneSteps([]);

    const stepDuration = 3500; // ms per step
    const timers = [];

    LOADING_STEPS.forEach((_, idx) => {
      if (idx === 0) return;
      timers.push(
        setTimeout(() => {
          setDoneSteps((prev) => [...prev, idx - 1]);
          setCurrentStep(idx);
        }, idx * stepDuration)
      );
    });

    return () => timers.forEach(clearTimeout);
  }, [loading]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    if (errors[name]) setErrors((prev) => ({ ...prev, [name]: undefined }));
  };

  const loadSample = () => {
    setFormData(SAMPLE_DATA);
    setErrors({});
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const validationErrors = validate(formData);
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      // Scroll to first error
      const firstKey = Object.keys(validationErrors)[0];
      document.getElementById(`field-${firstKey}`)?.focus();
      return;
    }
    setErrors({});
    setLoading(true);
    try {
      const response = await api.post("/evaluate", formData);
      onResult(response.data);
    } catch (err) {
      const msg =
        err?.response?.data?.message ||
        "The evaluation could not be completed. Please check the backend is running and your API key is set.";
      onError(msg);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-section">
      <div className="form-intro">
        <h2>Evaluate Your Startup</h2>
        <p>
          Submit your startup details for a comprehensive multi-agent AI analysis covering
          market potential, investment readiness, and matched government schemes.
        </p>
      </div>

      <div className="form-card">
        <form onSubmit={handleSubmit} noValidate>
          <div className="form-grid">
            {/* Startup Name */}
            <div className="form-group full-width">
              <label className="form-label" htmlFor="field-startup_name">
                Startup Name <span>*</span>
              </label>
              <input
                id="field-startup_name"
                className={`form-input${errors.startup_name ? " has-error" : ""}`}
                name="startup_name"
                placeholder="e.g. FarmAI, MediSense, EduPath"
                value={formData.startup_name}
                onChange={handleChange}
                disabled={loading}
                autoComplete="off"
              />
              {errors.startup_name && <p className="form-error">{errors.startup_name}</p>}
            </div>

            {/* Problem */}
            <div className="form-group full-width">
              <label className="form-label" htmlFor="field-problem">
                Problem Statement <span>*</span>
              </label>
              <textarea
                id="field-problem"
                className={`form-textarea${errors.problem ? " has-error" : ""}`}
                name="problem"
                placeholder="What specific, real-world problem are you solving? Who experiences it?"
                value={formData.problem}
                onChange={handleChange}
                disabled={loading}
                rows={3}
              />
              {errors.problem && <p className="form-error">{errors.problem}</p>}
            </div>

            {/* Solution */}
            <div className="form-group full-width">
              <label className="form-label" htmlFor="field-solution">
                Solution <span>*</span>
              </label>
              <textarea
                id="field-solution"
                className={`form-textarea${errors.solution ? " has-error" : ""}`}
                name="solution"
                placeholder="How does your product/service solve this problem? What makes it unique?"
                value={formData.solution}
                onChange={handleChange}
                disabled={loading}
                rows={3}
              />
              {errors.solution && <p className="form-error">{errors.solution}</p>}
            </div>

            {/* Industry */}
            <div className="form-group">
              <label className="form-label" htmlFor="field-industry">
                Industry <span>*</span>
              </label>
              <select
                id="field-industry"
                className={`form-select${errors.industry ? " has-error" : ""}`}
                name="industry"
                value={formData.industry}
                onChange={handleChange}
                disabled={loading}
              >
                <option value="">— Select Industry —</option>
                {INDUSTRIES.map((ind) => (
                  <option key={ind} value={ind}>{ind}</option>
                ))}
              </select>
              {errors.industry && <p className="form-error">{errors.industry}</p>}
            </div>

            {/* Stage */}
            <div className="form-group">
              <label className="form-label" htmlFor="field-stage">
                Startup Stage <span>*</span>
              </label>
              <select
                id="field-stage"
                className={`form-select${errors.stage ? " has-error" : ""}`}
                name="stage"
                value={formData.stage}
                onChange={handleChange}
                disabled={loading}
              >
                <option value="">— Select Stage —</option>
                {STAGES.map((s) => (
                  <option key={s} value={s}>{s}</option>
                ))}
              </select>
              {errors.stage && <p className="form-error">{errors.stage}</p>}
            </div>

            {/* Business Model */}
            <div className="form-group">
              <label className="form-label" htmlFor="field-business_model">
                Business Model <span>*</span>
              </label>
              <input
                id="field-business_model"
                className={`form-input${errors.business_model ? " has-error" : ""}`}
                name="business_model"
                placeholder="e.g. B2B SaaS, Freemium, Marketplace, D2C"
                value={formData.business_model}
                onChange={handleChange}
                disabled={loading}
              />
              {errors.business_model && <p className="form-error">{errors.business_model}</p>}
            </div>

            {/* Target Customers */}
            <div className="form-group">
              <label className="form-label" htmlFor="field-target_customers">
                Target Customers <span>*</span>
              </label>
              <input
                id="field-target_customers"
                className={`form-input${errors.target_customers ? " has-error" : ""}`}
                name="target_customers"
                placeholder="e.g. Small farmers, Urban millennials, SMB owners"
                value={formData.target_customers}
                onChange={handleChange}
                disabled={loading}
              />
              {errors.target_customers && <p className="form-error">{errors.target_customers}</p>}
            </div>
          </div>

          <div className="form-actions">
            {loading && (
              <div className="loading-steps">
                {LOADING_STEPS.map((step, idx) => (
                  <div
                    key={idx}
                    className={`loading-step ${
                      doneSteps.includes(idx) ? "done" : idx === currentStep ? "active" : ""
                    }`}
                  >
                    <span className="loading-step-icon">
                      {doneSteps.includes(idx) ? "✓" : idx === currentStep ? (
                        <span className="loading-step-spinner" />
                      ) : "·"}
                    </span>
                    {step}
                  </div>
                ))}
              </div>
            )}

            <button type="submit" className="btn-primary" disabled={loading}>
              {loading ? (
                <>
                  <span className="spinner" />
                  Evaluating...
                </>
              ) : (
                "Run Full Evaluation"
              )}
            </button>

            {!loading && (
              <button type="button" className="btn-secondary" onClick={loadSample}>
                Load Sample Startup
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
}

export default StartupForm;