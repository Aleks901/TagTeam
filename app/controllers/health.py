"""Health check controller."""

from litestar import Controller, get
from datetime import datetime, timezone


class HealthController(Controller):
    """Health check endpoints."""

    path = "/health"

    @get()
    async def health_check(self) -> dict[str, str]:
        """Check if the application is running."""
        return {
            "status": "healthy",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
