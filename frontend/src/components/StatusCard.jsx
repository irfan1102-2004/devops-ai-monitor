function StatusCard({ title, value }) {

  const getStatusColor = () => {

    if (title === "System Health") {

      if (value === "GOOD") {
        return "#22c55e";
      }

      if (value === "WARNING") {
        return "#eab308";
      }

      if (value === "CRITICAL") {
        return "#ef4444";
      }

    }


    if (title === "CPU Usage" || title === "Memory Usage") {

      const percentage = parseFloat(value);

      if (percentage < 50) {
        return "#22c55e";
      }

      if (percentage < 80) {
        return "#eab308";
      }

      return "#ef4444";

    }


    return "#38bdf8";

  };


  const color = getStatusColor();


  return (

    <div
      style={{
        backgroundColor: "#1e293b",
        padding: "25px",
        borderRadius: "15px",
        minWidth: "220px",
        boxShadow: "0 8px 20px rgba(0,0,0,0.4)",
        borderLeft: `6px solid ${color}`,
        transition: "0.3s",
      }}
    >

      <h3
        style={{
          color: "#cbd5e1",
          marginBottom: "15px",
        }}
      >
        {title}
      </h3>


      <h2
        style={{
          color: color,
          fontSize: "32px",
          margin: "0",
        }}
      >
        {value}
      </h2>


      <p
        style={{
          marginTop: "15px",
          color: "#94a3b8",
          fontSize: "14px",
        }}
      >
        🟢 Operational
      </p>


    </div>

  );

}


export default StatusCard;