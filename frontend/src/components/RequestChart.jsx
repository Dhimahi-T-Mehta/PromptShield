import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Cell,
} from "recharts";

function RequestChart({
  blocked,
  allowed,
}) {
  
  if(blocked.length===0 || allowed.length===0){
      return(
        <div className="empty-state">
        📊
        <h3>No analytics available</h3>
        <p>
        No security incidents match the current filters.
        </p>
        </div>
      )
  }
  
  const data = [
    {
      name: "Blocked",
      value: blocked,
      color: "#ef4444",
    },
    {
      name: "Allowed",
      value: allowed,
      color: "#22c55e",
    },
  ];

  return (
    <div className="chart-card">
      <h2>Blocked vs Allowed</h2>

      <ResponsiveContainer
        width="100%"
        height={320}
      >
        <BarChart
          data={data}
          layout="vertical"
          margin={{
            top: 10,
            right: 20,
            left: 20,
            bottom: 10,
          }}
        >
          <XAxis
            type="number"
            stroke="#9ca3af"
          />

          <YAxis
            type="category"
            dataKey="name"
            stroke="#9ca3af"
          />

          <Tooltip
            contentStyle={{
              background: "#111827",
              border: "1px solid #00ff9d",
              borderRadius: "10px",
              color: "#ffffff",
            }}
            formatter={(value, name, props) => [
              value,
              props.payload.name + " Requests",
            ]}
          />

          <Bar
            dataKey="value"
            radius={[0, 10, 10, 0]}
          >
            {data.map((entry, index) => (
              <Cell
                key={index}
                fill={entry.color}
              />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default RequestChart;