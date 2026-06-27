import {
    FaShieldAlt,
    FaExclamationTriangle,
    FaBrain,
    FaSearch,
    FaClipboardCheck,
    FaStickyNote,
    FaInfoCircle,
    FaCheckCircle
} from "react-icons/fa";
import { useState } from "react";
import "./ThreatExplanation.css";
import { exportIncident } from "../utils/exportIncident";

function ThreatExplanation({ attack }) {

    if (!attack) {
        return (
            <div className="threat-explanation-card">

                <h2>
                    <FaShieldAlt />
                    Incident Details
                </h2>

                <div className="empty-state">
                    Select an attack from the <strong>Recent Attacks</strong> table
                    to view its detailed explanation.
                </div>

            </div>
        );
    }

    const explanation = attack.explanation || {};

    const [copied, setCopied] = useState(false);

    const severity = explanation.severity || "LOW";

    const severityClass =
        explanation.severity?.toLowerCase() || "low";

    const modules = explanation.detection_modules || [];
    const matchedKeywords = explanation.matched_keywords || [];    
    
    const copyPrompt = async () => {

    if (!attack?.prompt) return;

    try {

        await navigator.clipboard.writeText(attack.prompt);

        setCopied(true);

        setTimeout(() => {

            setCopied(false);

        }, 2000);

    } catch (error) {

        console.error("Copy failed:", error);

    }

};
    
    return (

        <div className="threat-explanation-card">

            <h2>
                <FaShieldAlt />
                Incident Details
            </h2>

            <div className="overview-grid">

                <div className="overview-item">
                    <span>🚨 Attack Type</span>
                    <strong>{attack.attack_type?.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase())}
                    </strong>
                </div>

                <div className="overview-item">
                    <span>🛑 Action</span>
                    <span className={`action-badge ${attack.action.toLowerCase()}`}>
                        {attack.action}
                    </span>
                </div>

                <div className="overview-item">
                    <span>⚠ Severity</span>

                    <div
                        className={`severity-badge ${severity.toLowerCase()}`}
                    >
                        {severity}
                    </div>

                </div>

                <div className="overview-item">
                    <span>📊 Risk Score</span>
                    <strong>{attack.risk_score}</strong>
                </div>

                <div className="overview-item">
                    <span>🎯 Confidence</span>
                    <strong>{Math.round(attack.confidence * 100)}%</strong>
                </div>

                <div className="overview-item timestamp-item">
                    <span>🕒 Timestamp</span>
                    <strong>{attack.timestamp}</strong>
                </div>

        </div>

        <hr className="section-divider" />

        <div className="explanation-section">

            <div className="prompt-header">

    <div className="info-row">

        💬

        <span>Original Prompt</span>

    </div>

    <div className="prompt-actions">

        <button
            className={`copy-btn ${copied ? "copied" : ""}`}
            onClick={copyPrompt}
        >
            {copied ? "✔ Copied!" : "📋 Copy"}
        </button>

        <button
            className="export-btn"
            onClick={() => exportIncident(attack)}
        >
            📄 Export
        </button>

    </div>

</div>
            <div className="prompt-box">

                {attack.prompt}

            </div>

        </div>    
<hr className="section-divider" />
            <section className="explanation-section">

                <div className="info-row">
                    <FaInfoCircle />
                    <span>Summary</span>
                </div>

                <p>{explanation.summary}</p>

            </section>
<hr className="section-divider" />
            <section className="explanation-section">

                <div className="info-row">
                    <FaExclamationTriangle />
                    <span>Reason</span>
                </div>

                <p>{explanation.reason}</p>

            </section>
<hr className="section-divider" />
            <section className="explanation-section">

                <div className="info-row">
                    <FaBrain />
                    <span>Detection Modules</span>
                </div>

                <ul className="explanation-list">

                    <div className="chip-container">

                        {modules.map(module => (

                            <span
                                key={module}
                                className="keyword-chip"
                            >
                                🛡 {module}
                            </span>

                        ))}

                    </div>

                </ul>

            </section>
<hr className="section-divider" />
            {explanation.matched_keywords?.length > 0 && (

                <section className="explanation-section">

                    <div className="info-row">
                        <FaSearch />
                        <span>Matched Keywords</span>
                    </div>

                    <ul className="explanation-list">

                        <div className="chip-container">

                            {matchedKeywords.map(keyword => (

                                <span
                                    className="keyword-chip"
                                    key={keyword}
                                >
                                    {keyword}
                                </span>

                            ))}

                        </div>

                    </ul>

                </section>

            )}

            {explanation.detected_entities?.length > 0 && (

                <section className="explanation-section">

                    <div className="info-row">
                        <FaSearch />
                        <span>Detected Entities</span>
                    </div>

                    <ul className="explanation-list">

                        {explanation.detected_entities.map((entity, index) => (

                            <li key={index}>

                                <FaCheckCircle className="list-icon" />

                                {entity}

                            </li>

                        ))}

                    </ul>

                </section>

            )}
<hr className="section-divider" />
            <section className="explanation-section">

                <div className="info-row">
                    <FaClipboardCheck />
                    <span>Recommended Action</span>
                </div>

                <p>{explanation.recommended_action}</p>

            </section>
<hr className="section-divider" />
            <section className="explanation-section">

                <div className="info-row">
                    <FaStickyNote />
                    <span>Analyst Note</span>
                </div>

                <p>{explanation.analyst_note}</p>

            </section>

        </div>

    );
}

export default ThreatExplanation;