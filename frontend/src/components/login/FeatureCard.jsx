import { motion } from "framer-motion";

export default function FeatureCard({

    icon,

    title,

    text,

}) {

    return (

        <motion.div

            className="feature-card"

            whileHover={{

                y:-4,

                scale:1.02,

            }}

        >

            <div className="feature-icon">

                {icon}

            </div>

            <div>

                <h4>{title}</h4>

                <p>{text}</p>

            </div>

        </motion.div>

    );

}