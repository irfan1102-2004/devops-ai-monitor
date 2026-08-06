from fastapi import APIRouter, HTTPException

from app.ai.analyzer import analyze_system
from app.ai.loki_client import get_recent_logs

router = APIRouter()


@router.get("/analyze")
def analyze():
    try:
        return analyze_system()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/logs")
def logs():
    """
    Temporary endpoint to verify Loki integration.
    """
    try:
        return get_recent_logs()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))