from flask import jsonify


def success_response(data=None, message="OK", status_code=200):
    payload = {
        "success": True,
        "message": message,
        "data": data,
    }
    return jsonify(payload), status_code


def error_response(message="Something went wrong", status_code=500, details=None):
    payload = {
        "success": False,
        "message": message,
    }
    if details is not None:
        payload["details"] = details
    return jsonify(payload), status_code
