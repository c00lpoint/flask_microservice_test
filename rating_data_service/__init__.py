from flask import Flask
from flask_restful import Api
from flask_eureka import Eureka

from common_utilities.utilities import register_eureka_service
from rating_data_service.configs import FlaskConfig, ApplicationConfig
from rating_data_service.services import RatingDataService, UserRatingService


def create_app():
    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
    api = Api(app)
    # eureka = Eureka(app)

    # add routes
    api.add_resource(RatingDataService, '/rating/<int:movie_id>')
    api.add_resource(UserRatingService, '/rating/user/<string:user_id>')

    # register eureka
    # eureka.register_service()  # this method not support with windows env
    register_eureka_service(app_name=ApplicationConfig.APP_NAME, instance_port=ApplicationConfig.SERVICE_PORT)

    return app
