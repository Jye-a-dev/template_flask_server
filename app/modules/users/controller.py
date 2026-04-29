from flask import abort

from app.helpers.response import success_response
from app.modules.users.service import get_user, list_users


def index():
    return success_response(list_users(), "Users fetched successfully")


def show(user_id):
    user = get_user(user_id)
    if user is None:
        abort(404, description="User not found")
    return success_response(user, "User fetched successfully")
