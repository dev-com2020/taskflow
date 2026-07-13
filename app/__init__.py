from flask import Flask


def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config["TESTING"] = True

    from .routes import bp
    app.register_blueprint(bp)

    return app
