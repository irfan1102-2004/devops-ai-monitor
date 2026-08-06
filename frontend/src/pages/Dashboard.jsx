import { useEffect, useState } from "react";
import api from "../services/api";
import StatusCard from "../components/StatusCard";
import MetricsChart from "../components/MetricsChart";
import "./Dashboard.css";

function Dashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchAnalysis();

    const interval = setInterval(() => {
      fetchAnalysis();
    }, 5000);

    return () => clearInterval(interval);
  }, []);


  const fetchAnalysis = async () => {
    try {
      setError("");

      const response = await api.get("/ai/analyze");

      setData(response.data);
      setLoading(false);

    } catch (err) {

      console.error("Error fetching AI analysis:", err);

      setError("Unable to connect to the backend.");
      setLoading(false);

    }
  };


  return (

    <div className="dashboard">

      <h1 className="dashboard-title">
        📊 AI DevOps Monitoring Dashboard
      </h1>


      <hr className="dashboard-line" />


      {loading ? (

        <div className="loading">
          ⏳ Loading AI Analysis...
        </div>


      ) : error ? (

        <div className="error-box">
          ❌ {error}
        </div>


      ) : (

        <>


          {/* Status Cards */}

          <div className="cards-container">

            <StatusCard
              title="System Health"
              value={data.system_health}
            />


            <StatusCard
              title="CPU Usage"
              value={`${data.cpu_usage_percent}%`}
            />


            <StatusCard
              title="Memory Usage"
              value={`${data.memory_usage_percent}%`}
            />

          </div>



          {/* Metrics Chart */}

          <div className="chart-container">

            <MetricsChart
              cpu={data.cpu_usage_percent}
              memory={data.memory_usage_percent}
            />

          </div>




          {/* AI Recommendations */}

          <h2 className="section-title">
            🤖 AI Recommendations
          </h2>



          <div className="recommendations-container">


            {data.recommendations &&
            data.recommendations.length > 0 ? (


              data.recommendations.map((item,index)=>(

                <div
                  key={index}
                  className="ai-warning-card"
                >

                  <p>
                    ⚠️ {item}
                  </p>

                </div>

              ))


            ) : (


              <div className="ai-card">

                <p>
                  ✅ System is healthy.
                  <br />
                  No recommendations at this time.
                </p>

              </div>


            )}


          </div>


        </>

      )}


    </div>

  );

}


export default Dashboard;