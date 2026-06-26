import {
    FaShieldAlt,
    FaChartLine,
    FaBug,
    FaExclamationTriangle,
    FaDatabase,
    FaLock,
} from "react-icons/fa";

import "./ThreatIntelCards.css";

const formatAttackName = (text) => {

    if (!text) return "None";

    return text
        .split("_")
        .map(
            word =>
                word.charAt(0).toUpperCase() +
                word.slice(1)
        )
        .join(" ");

};

function ThreatIntelCards({ intelligence }) {

    if (!intelligence) {

        return (

            <div className="intel-container">

                <h2>Threat Intelligence</h2>

                <div className="intel-loading">

                    Loading threat intelligence...

                </div>

            </div>

        );

    }

    return (


        <div className="intel-container">

            <h2>

                <FaShieldAlt />

                Threat Intelligence

            </h2>

            <div className="intel-grid">

                <div className="intel-card">

                    <FaShieldAlt className="intel-icon" />

                    <span>Threat Level</span>

                    <h3>{intelligence.current_threat_level}</h3>

                </div>

                <div className="intel-card">

                    <FaChartLine className="intel-icon" />

                    <span>Average Risk</span>

                    <h3>

                        {intelligence.average_risk_score}

                    </h3>

                </div>

                <div className="intel-card">

                    <FaBug className="intel-icon" />

                    <span>Top Attack</span>

                    <h3>{formatAttackName(intelligence.most_frequent_attack)}</h3>
                </div>

                <div className="intel-card">

                    <FaExclamationTriangle className="intel-icon" />

                    <span>Latest Attack</span>

                    <h3>{formatAttackName(intelligence.latest_attack)}</h3>

                </div>

                <div className="intel-card">

                    <FaDatabase className="intel-icon" />

                    <span>Total Incidents</span>

                    <h3>

                        {intelligence.total_incidents}

                    </h3>

                </div>

                <div className="intel-card">

                    <FaLock className="intel-icon" />

                    <span>Block Rate</span>

                    <h3>

                        {intelligence.blocked_percentage}%

                    </h3>

                </div>

            </div>

        </div>

    );

}

export default ThreatIntelCards;