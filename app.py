from flask import Flask

from db import db
from views import main_bp


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(main_bp)
    # configure_app(application)
    return app


# def configure_app(application: Flask):
#     db.init_app(application)
#     api = Api(application)
#     api.add_namespace(director_ns)
#     api.add_namespace(genre_ns)
#     api.add_namespace(movie_ns)
#     api.add_namespace(user_ns)
#     api.add_namespace(auth_ns)
#     with application.app_context():
#         db.create_all()