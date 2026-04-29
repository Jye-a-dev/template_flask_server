from werkzeug.exceptions import HTTPException

from app.helpers.response import error_response


def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        return error_response(error.description, error.code)

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        app.logger.exception(error)
        return error_response("Internal server error", 500)
