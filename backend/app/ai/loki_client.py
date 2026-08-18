import os
import requests

LOKI_URL = os.getenv("LOKI_URL", "http://loki:3100")


def query_loki(query: str, limit: int = 100):
    response = requests.get(
        f"{LOKI_URL}/loki/api/v1/query",
        params={
            "query": query,
            "limit": limit,
        },
        timeout=10,
    )

    response.raise_for_status()
    return response.json()


def get_recent_logs(limit: int = 50):
    """
    Return a simplified list of recent log messages.
    """
    data = query_loki('{job=~".+"}', limit)

    logs = []

    for stream in data.get("data", {}).get("result", []):
        labels = stream.get("stream", {})

        for timestamp, message in stream.get("values", []):
            logs.append(
                {
                    "timestamp": timestamp,
                    "job": labels.get("job", "unknown"),
                    "service": labels.get("service_name", "unknown"),
                    "message": message.strip(),
                }
            )

    return logs
