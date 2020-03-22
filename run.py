import logging

from flask import Flask
from flask_jwt import JWT

from config import LOG_NAME
from service.JWTService import authenticate, identity


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from data.Model import db
    db.init_app(app)

    app.config['SECRET_KEY'] = 'strong key'
    jwt = JWT(app, authenticate, identity)

    logging.basicConfig(filename=LOG_NAME, level=logging.INFO)
    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
