from flask import Flask
from flask_restful import Api

from common_utilities.utilities import register_eureka_service
from movie_catalog_service.configs import FlaskConfig, ApplicationConfig
from movie_catalog_service.services import MovieCatalogService


def create_app():
    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
    api = Api(app)
    # eureka = Eureka(app)

    # add routes
    api.add_resource(MovieCatalogService, '/catalog/<string:user_name>')

    # register eureka
    register_eureka_service(app_name=ApplicationConfig.APP_NAME, instance_port=ApplicationConfig.SERVICE_PORT)

    return app