from app.ai.loki_client import get_recent_logs


def is_error_log(message: str) -> bool:
    """
    Detect real error conditions.
    """

    message = message.lower()

    error_patterns = [
        "level=error",
        "\"level\":\"error\"",
        "traceback",
        "exception",
        "failed",
        "failure",
        "connection refused",
        "timeout",
        "500 internal server error",
        "http 500",
    ]

    return any(pattern in message for pattern in error_patterns)


def is_warning_log(message: str) -> bool:
    """
    Detect warning conditions.
    """

    message = message.lower()

    warning_patterns = [
        "level=warning",
        "level=warn",
        "\"level\":\"warning\"",
        "deprecated",
        "retry",
        "slow response",
    ]

    return any(pattern in message for pattern in warning_patterns)


def analyze_logs(limit: int = 100):
    """
    Analyze recent logs for errors and warnings.
    """

    logs = get_recent_logs(limit)

    error_logs = []
    warning_logs = []

    for log in logs:
        message = log.get("message", "")

        if is_error_log(message):
            error_logs.append(log)

        elif is_warning_log(message):
            warning_logs.append(log)

    return {
        "recent_errors": len(error_logs),
        "recent_warnings": len(warning_logs),
        "error_logs": error_logs[:10],
        "warning_logs": warning_logs[:10],
    }