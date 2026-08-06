from app.ai.prometheus_client import (
    get_cpu_usage,
    get_memory_usage,
    get_targets_status,
)
from app.ai.log_analyzer import analyze_logs


def analyze_system():
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    targets = get_targets_status()

    alerts = []
    analysis = []
    recommendations = []

    # -------------------------
    # Metrics Analysis
    # -------------------------

    if cpu > 80:
        alerts.append("High CPU usage detected.")
        analysis.append(f"CPU usage is high ({cpu:.2f}%).")
        recommendations.append("Investigate processes consuming CPU.")
    else:
        analysis.append(f"CPU usage is normal ({cpu:.2f}%).")

    if memory > 80:
        alerts.append("High memory usage detected.")
        analysis.append(f"Memory usage is high ({memory:.2f}%).")
        recommendations.append("Check for memory leaks or increase available RAM.")
    else:
        analysis.append(f"Memory usage is healthy ({memory:.2f}%).")

    unhealthy_targets = [t for t in targets if t.get("health") != "up"]

    if unhealthy_targets:
        alerts.append("Some monitored services are down.")
        analysis.append(f"{len(unhealthy_targets)} monitored target(s) are unhealthy.")
        recommendations.append("Check Prometheus targets and affected services.")
    else:
        analysis.append("All monitored services are operational.")

    # -------------------------
    # Log Analysis
    # -------------------------

    log_report = analyze_logs()

    if log_report["recent_errors"] > 0:
        alerts.append(f'{log_report["recent_errors"]} error log(s) detected.')
        recommendations.append("Investigate recent application errors.")

    if log_report["recent_warnings"] > 0:
        recommendations.append("Review warning logs before they become critical.")

    # -------------------------
    # Overall Health
    # -------------------------

    if alerts:
        system_health = "WARNING"
    else:
        system_health = "GOOD"

    return {
        "system_health": system_health,
        "cpu_usage_percent": round(cpu, 2),
        "memory_usage_percent": round(memory, 2),
        "alerts": alerts,
        "analysis": analysis,
        "recommendations": recommendations,
        "recent_errors": log_report["recent_errors"],
        "recent_warnings": log_report["recent_warnings"],
        "error_logs": log_report["error_logs"],
        "warning_logs": log_report["warning_logs"],
    }