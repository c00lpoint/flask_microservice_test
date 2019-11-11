from flask import Flask
from flask_restful import Api

from movie_data_service.configs import ServiceConfig
from movie_data_service.services import MovieDataService


def create_app(name):
    app = Flask(name)
    app.config.from_object(ServiceConfig)
    api = Api(app)

    # add routes
    api.add_resource(MovieDataService, '/movie/<int:movie_id>')

    # register eureka service

    return app
