import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from "recharts";

const COLORS = {
  safe: "#22c55e",
  prompt_injection: "#ef4444",
  jailbreak: "#f97316",
  pii_extraction: "#a855f7",
  role_manipulation: "#eab308",
};

const formatLabel = (name) =>
  name
    .replace(/_/g, " ")
    .replace(/\b\w/g, (char) => char.toUpperCase());

function AttackDistribution({ data }) {
  return (
    <div className="chart-card">
      <h2>Attack Distribution</h2>

      <ResponsiveContainer
        width="100%"
        height={350}
      >
        <PieChart>
          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            innerRadius={60}
            outerRadius={120}
            paddingAngle={3}
            label
          >
            {data.map((entry, index) => (
              <Cell
                key={index}
                fill={
                  COLORS[entry.name] || "#00ff9d"
                }
              />
            ))}
          </Pie>

          <Tooltip />

          <Legend
            verticalAlign="bottom"
            height={50}
            formatter={(value) =>
              formatLabel(value)
            }
          />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}

export default AttackDistribution;