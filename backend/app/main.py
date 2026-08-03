from fastapi import FastAPI

app = FastAPI(
    title="AI DevOps Monitoring API",
    description="Backend API for AI-powered DevOps Monitoring System",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to the AI DevOps Monitoring API 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }