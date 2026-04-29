from app.modules.users.model import User


_USERS = [
    User(id=1, name="Demo User", email="demo@example.com"),
]


def list_users():
    return [user.to_dict() for user in _USERS]


def get_user(user_id):
    for user in _USERS:
        if user.id == user_id:
            return user.to_dict()
    return None
