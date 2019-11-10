from flask_restful import Resource, abort
import requests

from common_utilities.constants import RatingProperties, UserRatingProperties

rating_movie_samples = [
    {RatingProperties.MOVIE_ID: 24428, RatingProperties.RATING: 3.8},
    {RatingProperties.MOVIE_ID: 99861, RatingProperties.RATING: 3.7},
    {RatingProperties.MOVIE_ID: 299536, RatingProperties.RATING: 4.2},
    {RatingProperties.MOVIE_ID: 299534, RatingProperties.RATING: 4.2},
]


class RatingDataService(Resource):

    def get(self, movie_id):
        return {RatingProperties.MOVIE_ID: movie_id, RatingProperties.RATING: 3.8}


class UserRatingService(Resource):

    def get(self, user_id):
        return {
            UserRatingProperties.USER_ID: user_id,
            UserRatingProperties.RATINGS: rating_movie_samples
        }
