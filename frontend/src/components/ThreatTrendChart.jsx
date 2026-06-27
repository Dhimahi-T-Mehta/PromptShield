import {
    ResponsiveContainer,
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
} from "recharts";

import "./ThreatTrendChart.css";

function ThreatTrendChart({ data }) {

    if (!data || data.length === 0) {

        return (

            <div className="trend-card">

                <h2>Threat Trend Analytics</h2>

                <div className="trend-loading">

                    No trend data available.

                </div>

            </div>

        );

    }

    return (

        <div className="trend-card">

            <h2>Threat Trend Analytics</h2>

            <ResponsiveContainer
                width="100%"
                height={340}
            >

                <LineChart data={data}>

                    <CartesianGrid
                        strokeDasharray="3 3"
                        stroke="#333"
                    />

                    <XAxis dataKey="date" />

                    <YAxis />

                    <Tooltip />

                    <Legend />

                    <Line
                        type="monotone"
                        dataKey="requests"
                        stroke="#00e5ff"
                        strokeWidth={3}
                        dot={{ r: 5 }}
                        activeDot={{ r: 8 }}
                    />

                    <Line
                        type="monotone"
                        dataKey="blocked"
                        stroke="#ef4444"
                        strokeWidth={3}
                        dot={{ r: 5 }}
                        activeDot={{ r: 8 }}
                    />

                    <Line
                        type="monotone"
                        dataKey="allowed"
                        stroke="#22c55e"
                        strokeWidth={3}
                        dot={{ r: 5 }}
                        activeDot={{ r: 8 }}
                    />

                </LineChart>

            </ResponsiveContainer>

        </div>

    );

}

export default ThreatTrendChart;