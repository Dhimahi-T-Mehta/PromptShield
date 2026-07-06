import {
    FaShieldAlt,
    FaCircle,
    FaRobot,
    FaDatabase
} from "react-icons/fa";

function HeroSection({

    threatLevel,

    protectionScore,

    lastUpdated

}) {

    return (

        <div className="hero-section">

    <div className="hero-left">

        <div className="hero-stat">
            <FaCircle className="online-dot" />
            <span>Protection Active</span>
        </div>

        <div className="hero-stat">
            <FaRobot />
            <strong>Threat Level:</strong>
            <span>{threatLevel}</span>
        </div>

        <div className="hero-stat">
            <FaShieldAlt />
            <strong>Protection Score:</strong>
            <span>{protectionScore}%</span>
        </div>

        <div className="hero-stat">
            <FaDatabase />
            <strong>Last Updated:</strong>
            <span>{lastUpdated}</span>
        </div>

    </div>

    <div className="hero-right">

        <div className="hero-title">

            <FaShieldAlt className="hero-logo"/>

            <div>

                <h1>PROMPTSHIELD</h1>

                <h2>AI SECURITY MIDDLEWARE</h2>

            </div>

        </div>

        <p>

            Enterprise-grade LLM Firewall for detecting
            Prompt Injection, Jailbreak Attacks,
            PII Extraction, Role Manipulation and
            Prompt Sanitization in real time.

        </p>

    </div>

</div>

    );

}

export default HeroSection;