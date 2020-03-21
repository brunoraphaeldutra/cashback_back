import logging

from flask import Flask

from config import LOG_NAME


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from data.Model import db
    db.init_app(app)

    logging.basicConfig(filename=LOG_NAME, level=logging.INFO)
    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)