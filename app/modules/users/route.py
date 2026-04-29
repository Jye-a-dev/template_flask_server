from flask import Blueprint

from app.modules.users.controller import index, show


users_bp = Blueprint("users", __name__)

users_bp.get("/")(index)
users_bp.get("/<int:user_id>")(show)
