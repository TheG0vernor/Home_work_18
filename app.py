from flask import Flask
from flask_restx import Api

from config import Config
from views.director_views import director_ns
from views.genre_views import genre_ns
from views.movie_views import movie_ns
from setup_db import db


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    configure_app(app)
    return app


def configure_app(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


if __name__ == '__main__':
    app = create_app(Config)
    app.run(port=10000)
