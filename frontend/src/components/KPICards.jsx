import {
    FaDatabase,
    FaBan,
    FaCheckCircle,
    FaChartLine,
    FaShieldAlt
} from "react-icons/fa";

import { motion } from "framer-motion";

function Card({ card, index }) {

    return (

        <motion.div

            className="kpi-card"

            initial={{
                opacity: 0,
                y: 20
            }}

            animate={{
                opacity: 1,
                y: 0
            }}

            transition={{
                duration: 0.35,
                delay: index * 0.08
            }}

            whileHover={{
                scale: 1.04
            }}

        >

            {card.icon}

            <h3>{card.title}</h3>

            <h2>{card.value}</h2>

        </motion.div>

    );

}

function KPICards({

    totalRequests,
    blockedRequests,
    allowedRequests,
    detectionRate,
    protectionScore

}) {

    const firstRow = [

        {
            title: "Total Requests",
            value: totalRequests,
            icon: <FaDatabase className="kpi-icon" />
        },

        {
            title: "Blocked Requests",
            value: blockedRequests,
            icon: <FaBan className="kpi-icon danger" />
        },

        {
            title: "Allowed Requests",
            value: allowedRequests,
            icon: <FaCheckCircle className="kpi-icon success" />
        }

    ];

    const secondRow = [

        {
            title: "Detection Rate",
            value: `${detectionRate}%`,
            icon: <FaChartLine className="kpi-icon" />
        },

        {
            title: "Protection Score",
            value: `${protectionScore}%`,
            icon: <FaShieldAlt className="kpi-icon success" />
        }

    ];

    return (

        <>

            <div className="kpi-grid first-row">

                {firstRow.map((card, index) => (

                    <Card
                        key={card.title}
                        card={card}
                        index={index}
                    />

                ))}

            </div>

            <div className="kpi-grid second-row">

                {secondRow.map((card, index) => (

                    <Card
                        key={card.title}
                        card={card}
                        index={index + 3}
                    />

                ))}

            </div>

        </>

    );

}

export default KPICards;