from flask import Flask
from .api.routes import api_bp
from .views import view_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_bp)
    app.register_blueprint(view_bp)

    return app
