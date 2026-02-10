"""Main application entry point for the Litestar application."""
from litestar import Litestar, get
from litestar.config.cors import CORSConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig
from app.controllers.health import HealthController
from app.controllers.items import ItemController


@get("/")
async def index() -> dict[str, str]:
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to Litestar!", "docs": "/schema"}


# CORS configuration
cors_config = CORSConfig(
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the Litestar application
app = Litestar(
    route_handlers=[
        index,
        HealthController,
        ItemController,
    ],
    cors_config=cors_config,
    debug=True,
)
