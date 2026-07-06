import {
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
} from "recharts";
import { FaShieldAlt } from "react-icons/fa";
import "./DetectionModuleStats.css";
import { Cell } from "recharts";
const COLORS = [
                "#00E5FF",
                "#22C55E",
                "#F97316",
                "#A855F7",
            ];

function DetectionModuleStats({ data }) {

    if (!data) {

        return (

            <div className="module-card">

                <h2>🛡 Detection Module Statistics</h2>

                <div className="module-loading">

                    Loading statistics...

                </div>

            </div>

        );

    }

    const chartData = [

        {
            module: "DistilBERT",
            detections: data["DistilBERT"] || 0,
        },

        {
            module: "Presidio",
            detections: data["Presidio"] || 0,
        },

        {
            module: "Jailbreak",
            detections: data["Jailbreak Rule Engine"] || 0,
        },

        {
            module: "Role Engine",
            detections: data["Role Manipulation Rule Engine"] || 0,
        },

    ];

    const totalDetections = chartData.reduce(

    (sum, item) => sum + item.detections,

    0

    );

    return (

        <div className="module-card">

            <h2>Detection Module Statistics</h2>
            <p className="module-total">
                Total Detections: {totalDetections}
            </p>

            <ResponsiveContainer
                width="100%"
                height={320}
            >


                <BarChart
                    data={chartData}
                    layout="vertical"
                >

                    <CartesianGrid
                        strokeDasharray="3 3"
                        stroke="#333"
                    />

                    <XAxis
                        type="number"
                    />

                    <YAxis
                        type="category"
                        dataKey="module"
                        width={120}
                    />

                    <Tooltip />

                    <Bar
                        dataKey="detections"
                        radius={[0, 8, 8, 0]}
                    >
                        {chartData.map((entry, index) => (

                            <Cell
                                key={index}
                                fill={COLORS[index]}
                            />

                        ))}
                    </Bar>

                </BarChart>

            </ResponsiveContainer>

        </div>

    );

}

export default DetectionModuleStats;