from app import create_app
from app.config.env import config


app = create_app()


if __name__ == "__main__":
    app.run(host=config.host, port=config.port, debug=config.debug)
