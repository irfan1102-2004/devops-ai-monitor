import requests

PROMETHEUS_URL = "http://prometheus:9090"


def query_prometheus(query: str):
    response = requests.get(
        f"{PROMETHEUS_URL}/api/v1/query",
        params={"query": query},
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


def _extract_single_value(response_json):
    results = response_json.get("data", {}).get("result", [])

    if not results:
        return 0.0

    return float(results[0]["value"][1])


def get_cpu_usage():
    response = query_prometheus(
        'sum(rate(node_cpu_seconds_total{mode!="idle",mode!="iowait"}[5m])) / count(node_cpu_seconds_total{mode="idle"}) * 100'
    )

    return _extract_single_value(response)


def get_memory_usage():
    response = query_prometheus(
        '(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100'
    )

    return _extract_single_value(response)


def get_targets_status():
    response = query_prometheus("up")

    targets = []

    for item in response.get("data", {}).get("result", []):
        status = item["value"][1]

        targets.append(
            {
                "job": item["metric"].get("job"),
                "instance": item["metric"].get("instance"),
                "health": "up" if status == "1" else "down",
            }
        )

    return targets