import { motion } from "framer-motion";
import LoginForm from "./LoginForm";

export default function LoginCard() {
    return (
        <motion.div
            className="login-card"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{
                duration: 0.7,
                ease: "easeOut",
            }}
        >
            <div className="login-card-header">

                <h1>Welcome Back</h1>

                <p>
                    Sign in to PromptShield SOC
                </p>

            </div>

            <div className="login-divider" />

            <LoginForm />

            <div className="login-footer">

                <span>Powered by</span>

                <strong>
                    PromptShield Security Platform
                </strong>

            </div>

        </motion.div>
    );
}