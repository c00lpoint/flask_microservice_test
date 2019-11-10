from flask import Flask
from flask_restful import Api

from rating_data_service.services import RatingDataService, UserRatingService


def create_app(name):
    app = Flask(name)
    api = Api(app)

    api.add_resource(RatingDataService, '/rating/<int:movie_id>')
    api.add_resource(UserRatingService, '/rating/user/<string:user_id>')

    return app
