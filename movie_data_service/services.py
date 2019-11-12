from flask_restful import Resource, abort
import requests

from movie_data_service.configs import ExternalServiceUrls
from movie_data_service.constants import TmdbMovieProperties
from common_utilities.constants import MovieProperties


class MovieDataService(Resource):

    def get(self, movie_id):
        tmdb_move_service_url = ExternalServiceUrls.TMDB_MOVIE_SEARCH_URL_FORMAT % movie_id
        rps = requests.get(tmdb_move_service_url)
        if rps.ok:
            tmdb_movie_info = rps.json()
            return {
                MovieProperties.ID: tmdb_movie_info.get(TmdbMovieProperties.ID),
                MovieProperties.NAME: tmdb_movie_info.get(TmdbMovieProperties.ORI_TITLE),
                MovieProperties.DESC: tmdb_movie_info.get(TmdbMovieProperties.OVERVIEW)
            }
        else:
            abort(rps.status_code, message='cannot get movie information from tmdb service.')
