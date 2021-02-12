from flask import Flask
from flask_bcrypt import Bcrypt
from app.main.config.server_config import config

flask_bcrypt = Bcrypt()


def create_app(process_env):
    """앱 초기화 및 실행"""
    app = Flask(__name__)
    app.config.from_object(config[process_env])
    flask_bcrypt.init_app(app)

    return app
