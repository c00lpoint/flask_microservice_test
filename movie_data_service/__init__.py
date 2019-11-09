from flask import Flask
from flask_restful import Api

from movie_data_service.services import MovieDataService


def create_app(name):
    app = Flask(name)
    api = Api(app)

    api.add_resource(MovieDataService, '/movie/<int:movie_id>')
    return app
