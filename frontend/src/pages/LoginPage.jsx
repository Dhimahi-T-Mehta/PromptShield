import HeroPanel from "../components/login/HeroPanel";
import LoginCard from "../components/login/LoginCard";
import CyberBackground from "../components/login/CyberBackground";

import "../styles/login.css";

export default function LoginPage() {
    return (
        <div className="login-page">

            <CyberBackground />

           <main className="login-container">

                <HeroPanel />

                <LoginCard />

            </main>

        </div>
    );
}