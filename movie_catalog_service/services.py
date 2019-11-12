from flask_restful import Resource, abort
from py_eureka_client import eureka_client

from movie_catalog_service.configs import EurekaServiceName
from common_utilities.constants import UserRatingProperties, RatingProperties, \
    MovieProperties, \
    MovieCatalogProperties, MovieCatalogListProperties


def get_movie_catalog(movie_id, rating):
    movie_info = eureka_client.do_service(app_name=EurekaServiceName.MOVIE_DATA,
                                          service=f'movie/{movie_id}',
                                          return_type='json')
    return {
        MovieCatalogProperties.MOVIE_NAME: movie_info[MovieProperties.NAME],
        MovieCatalogProperties.MOVIE_DESC: movie_info[MovieProperties.DESC],
        MovieCatalogProperties.MOVIE_RATING: rating
    }


class MovieCatalogService(Resource):

    def get(self, user_name):
        user_ratings = eureka_client.do_service(app_name=EurekaServiceName.RATING_DATA,
                                                service=f'rating/user/{user_name}',
                                                return_type='json')
        movie_ratings = user_ratings[UserRatingProperties.RATINGS]
        movie_catalogs = [get_movie_catalog(movie_rating[RatingProperties.MOVIE_ID],
                                            movie_rating[RatingProperties.RATING])
                          for movie_rating in movie_ratings]
        return {MovieCatalogListProperties.CATALOG_LIST: movie_catalogs}



