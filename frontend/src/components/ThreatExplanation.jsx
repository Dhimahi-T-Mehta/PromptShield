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

import "./ThreatExplanation.css";

function ThreatExplanation({ attack }) {

    if (!attack) {
        return (
            <div className="threat-explanation-card">

                <h2>
                    <FaShieldAlt />
                    Threat Explanation
                </h2>

                <div className="empty-state">
                    Select an attack from the <strong>Recent Attacks</strong> table
                    to view its detailed explanation.
                </div>

            </div>
        );
    }

    const explanation = attack.explanation || {};

    const severityClass =
        explanation.severity?.toLowerCase() || "low";

    return (

        <div className="threat-explanation-card">

            <h2>
                <FaShieldAlt />
                Threat Explanation
            </h2>

            <div className="severity-wrapper">
                <span className={`severity-badge ${severityClass}`}>
                    {explanation.severity}
                </span>
            </div>

            <section className="explanation-section">

                <div className="info-row">
                    <FaInfoCircle />
                    <span>Summary</span>
                </div>

                <p>{explanation.summary}</p>

            </section>

            <section className="explanation-section">

                <div className="info-row">
                    <FaExclamationTriangle />
                    <span>Reason</span>
                </div>

                <p>{explanation.reason}</p>

            </section>

            <section className="explanation-section">

                <div className="info-row">
                    <FaBrain />
                    <span>Detection Modules</span>
                </div>

                <ul className="explanation-list">

                    {explanation.detection_modules?.map((module, index) => (

                        <li key={index}>

                            <FaCheckCircle className="list-icon" />

                            {module}

                        </li>

                    ))}

                </ul>

            </section>

            {explanation.matched_keywords?.length > 0 && (

                <section className="explanation-section">

                    <div className="info-row">
                        <FaSearch />
                        <span>Matched Keywords</span>
                    </div>

                    <ul className="explanation-list">

                        {explanation.matched_keywords.map((keyword, index) => (

                            <li key={index}>

                                <FaCheckCircle className="list-icon" />

                                {keyword}

                            </li>

                        ))}

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

            <section className="explanation-section">

                <div className="info-row">
                    <FaClipboardCheck />
                    <span>Recommended Action</span>
                </div>

                <p>{explanation.recommended_action}</p>

            </section>

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