import { motion } from "framer-motion";

export default function CyberBackground() {

    return (

        <div className="cyber-background">

            <div className="cyber-grid"></div>

            <div className="network-lines">

                {

                    [...Array(8)].map((_, i)=>(

                        <span

                            key={i}

                            className={`line line-${i}`}

                        />

                    ))

                }

            </div>

            <div className="cyber-gradient"></div>

            {

                [...Array(18)].map((_, i) => (

                    <motion.span

                        key={i}

                        className="particle"

                        initial={{
                            opacity: 0,
                            x: Math.random() * window.innerWidth,
                            y: Math.random() * window.innerHeight,
                        }}

                        animate={{
                            opacity: [0, .8, 0],
                            y: [
                                Math.random() * window.innerHeight,
                                Math.random() * window.innerHeight - 180
                            ]
                        }}

                        transition={{
                            duration: 6 + Math.random() * 6,
                            repeat: Infinity,
                            delay: Math.random() * 5,
                        }}

                    />

                ))

            }

        </div>

    );

}