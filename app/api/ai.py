from fastapi import APIRouter

from app.ai.prometheus_client import (
    get_targets_status,
    get_cpu_usage,
    get_memory_usage,
)
from app.ai.analyzer import analyze_system

router = APIRouter()


@router.get("/analyze")
def analyze():
    cpu_data = get_cpu_usage()
    memory_data = get_memory_usage()
    status_data = get_targets_status()

    cpu = max(
        0,
        min(
            100,
            float(cpu_data["data"]["result"][0]["value"][1])
        )
    )

    memory = max(
        0,
        min(
            100,
            float(memory_data["data"]["result"][0]["value"][1])
        )
    )

    return analyze_system(
        cpu=cpu,
        memory=memory,
        targets=status_data["data"]["result"]
    )