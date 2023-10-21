"""
Main Application Runner
-----------------------

This module is responsible for running the Flask application. It imports
the application factory function from the app module and initializes it
with the default settings. The application is set to run in debug mode
when this module is executed directly.

Functions:
    - create_app(): Imported from the app module to create a Flask
    application instance.

Usage:
    python run.py
"""

from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
