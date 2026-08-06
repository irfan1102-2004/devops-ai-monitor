import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";


function MetricsChart({ cpu, memory }) {

  const data = [
    {
      name: "CPU",
      Usage: cpu,
    },
    {
      name: "Memory",
      Usage: memory,
    },
  ];


  return (

    <div
      style={{
        backgroundColor: "#1e293b",
        padding: "25px",
        borderRadius: "15px",
        marginTop: "30px",
        boxShadow: "0 8px 20px rgba(0,0,0,0.4)",
      }}
    >

      <h2
        style={{
          marginBottom: "20px",
          color: "#e2e8f0",
        }}
      >
        📈 System Metrics Overview
      </h2>


      <ResponsiveContainer
        width="100%"
        height={350}
      >

        <BarChart data={data}>

          <CartesianGrid
            strokeDasharray="3 3"
          />


          <XAxis
            dataKey="name"
            tick={{ fill: "#cbd5e1" }}
          />


          <YAxis
            domain={[0,100]}
            tick={{ fill: "#cbd5e1" }}
          />


          <Tooltip />


          <Bar
            dataKey="Usage"
            radius={[10,10,0,0]}
            fill="#38bdf8"
          />


        </BarChart>

      </ResponsiveContainer>


    </div>

  );

}


export default MetricsChart;