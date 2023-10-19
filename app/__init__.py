from flask import Flask, render_template
from .api.routes import api_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = 'klfopj90u49-=!@'

    app.register_blueprint(api_bp)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')
    return app
