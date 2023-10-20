from flask import Flask, render_template
from .api.routes import api_bp
from os import getenv


def create_app():
    """Creates and initializes an instance of the Flask application.

        - Sets a secret key for the application.
        - Registers the API Blueprint.
        - Defines and registers the main route that handles both GET
        and POST requests.

        Returns:
        Flask app: A configured instance of the Flask application.
        """
    app = Flask(__name__)
    app.secret_key = getenv('APP_SECRET_KEY')

    app.register_blueprint(api_bp)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        """Handles requests to the application's root route ('/').

        For a GET request, the 'index.html' template will be displayed.
        For a POST request, the sent data will be processed, 
        and subsequently, the 'index.html' template will be displayed 
        (unless another action is specified).

        Returns:
            template: Renders and returns the 'index.html' template.
        """
        return render_template('index.html')
    return app
