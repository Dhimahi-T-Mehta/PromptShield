import { motion } from "framer-motion";
import { FiShield } from "react-icons/fi";

export default function AnimatedShield() {
    return (
        <div className="shield-wrapper">
        <div className="shield-container hero-inline-shield hero-logo">

            {/* Outer Rotating Ring */}
            <motion.div
                className="shield-ring ring-1"
                animate={{ rotate: 360 }}
                transition={{
                    duration: 18,
                    repeat: Infinity,
                    ease: "linear",
                }}
            />

            {/* Inner Rotating Ring */}
            <motion.div
                className="shield-ring ring-2"
                animate={{ rotate: -360 }}
                transition={{
                    duration: 12,
                    repeat: Infinity,
                    ease: "linear",
                }}
            />

            {/* Pulse Effect */}
            <motion.div
                className="shield-pulse"
                animate={{
                    scale:[1,1.08,1],
                    opacity: [0.35, 0.08, 0.35],
                }}
                transition={{
                    duration: 2.8,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            />

            {/* Shield Icon */}
            <motion.div
                className="shield-core"
                animate={{
                    y:[0,-3,0],
                    scale: [1, 1.04, 1],
                }}
                transition={{
                    duration: 3,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            >
                <FiShield className="shield-icon" />
            </motion.div>

            {/* Orbiting Dots */}
            <motion.span
                className="orbit-dot dot-1"
                animate={{ rotate: 360 }}
                transition={{
                    duration: 8,
                    repeat: Infinity,
                    ease: "linear",
                }}
            />

            <motion.span
                className="orbit-dot dot-2"
                animate={{ rotate: -360 }}
                transition={{
                    duration: 10,
                    repeat: Infinity,
                    ease: "linear",
                }}
            />

            <motion.span
                className="orbit-dot dot-3"
                animate={{ rotate: 360 }}
                transition={{
                    duration: 13,
                    repeat: Infinity,
                    ease: "linear",
                }}
            />

            {/* Scan Line */}
            <motion.div
                className="shield-scan"
                animate={{
                    y: [-70, 70, -70],
                    opacity: [0, 1, 0],
                }}
                transition={{
                    duration: 3.5,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            />

        </div>
    </div>
    );
}