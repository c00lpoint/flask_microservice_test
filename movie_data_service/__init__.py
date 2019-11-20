from flask import Flask
from flask_restful import Api
from logging.config import dictConfig
from logging import getLogger

from common_utilities.utilities import register_eureka_service
from movie_data_service.configs import ApplicationConfig, FlaskConfig
from movie_data_service.services import MovieDataService


def create_app():
    dictConfig(ApplicationConfig.LOGGING)

    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
    api = Api(app)

    # add routes
    api.add_resource(MovieDataService, '/movie/<int:movie_id>')

    # register eureka service
    register_eureka_service(app_name=ApplicationConfig.APP_NAME, instance_port=ApplicationConfig.SERVICE_PORT)

    return app
