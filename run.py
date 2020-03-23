import logging

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import LOG_NAME, CPF_ADM, DEFAULT_PASSWORD, CREATE_FIRST_RESELLER
from service.ResellerService import ResellerService
from util.StringUtil import StringUtil


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from data.Model import db
    db.init_app(app)

    app.config['SECRET_KEY'] = 'strong key'
    JWTManager(app)
    CORS(app)
    logging.basicConfig(filename=LOG_NAME, level=logging.INFO)
    return app


app = create_app("config")


@app.before_first_request
def initial_reseller():
    if CREATE_FIRST_RESELLER:
        service = ResellerService()
        only_cpf = StringUtil.get_cpf(CPF_ADM)
        try:
            service.add(
                {"full_name": "Administrator", "cpf": only_cpf, "email": "{0}@email.com", "password": "{1}"
                    .format(only_cpf, DEFAULT_PASSWORD)})
        except Exception:
            pass


if __name__ == "__main__":
    app.run(debug=True)
