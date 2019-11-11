from flask import Flask
from flask_restful import Api
from flask_eureka import Eureka

from rating_data_service.configs import FlaskConfig
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

    return app
