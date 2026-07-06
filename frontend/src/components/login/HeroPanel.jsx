import AnimatedShield from "./AnimatedShield";
import FeatureCard from "./FeatureCard";
import {
    FiShield,
    FiLock,
    FiCpu,
    FiZap,
} from "react-icons/fi";

export default function HeroPanel() {

    return (

        <section className="hero-panel">

            <div className="hero-brand">

                <FiShield className="hero-logo" />

                <div className="hero-brand-text">

                    <h1 className="hero-title">
                        PromptShield
                    </h1>

                    <h2 className="hero-subtitle">
                        AI-Powered LLM Firewall
                    </h2>

                </div>

            </div>

            <p className="hero-description">

                Secure enterprise AI against
                Prompt Injection,
                Jailbreaks,
                Role Manipulation
                and PII Leakage.

            </p>

            <div className="hero-features">

                <FeatureCard
                    icon={<FiShield />}
                    title="Prompt Injection"
                    text="Stops malicious prompt manipulation."
                />

                <FeatureCard
                    icon={<FiZap />}
                    title="Jailbreak Detection"
                    text="Detects advanced bypass attempts."
                />

                <FeatureCard
                    icon={<FiLock />}
                    title="PII Protection"
                    text="Redacts sensitive information automatically."
                />

                <FeatureCard
                    icon={<FiCpu />}
                    title="Explainable AI"
                    text="Transparent security decisions."
                />

            </div>

        </section>

    );

}