import axios from "axios";

const api = axios.create({
  baseURL: "https://devops-ai-monitor.onrender.com/api/v1",
});

export default api;