from app.helpers.response import success_response
from app.modules.users.route import users_bp


def register_routes(app):
    @app.get("/")
    def index():
        return success_response(
            {
                "service": "server",
                "status": "running",
                "docs": {
                    "health": "/health",
                    "users": "/api/users",
                },
            },
            "Server is running",
        )

    @app.get("/health")
    def health():
        return success_response({"status": "ok"}, "Healthy")

    app.register_blueprint(users_bp, url_prefix="/api/users")
