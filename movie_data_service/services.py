from flask_restful import Resource
import requests

from .constants import ServiceUrls, TmdbMovieProperties
from constants import MovieProperties


class MovieDataService(Resource):

    def get(self, movie_id):
        tmdb_move_service_url = ServiceUrls.TMDB_MOVIE_SEARCH_URL_FORMAT % movie_id
        rps = requests.get(tmdb_move_service_url)
        if rps.ok:
            tmdb_movie_info = rps.json()
            return {
                MovieProperties.ID: tmdb_movie_info.get(TmdbMovieProperties.ID),
                MovieProperties.NAME: tmdb_movie_info.get(TmdbMovieProperties.ORI_TITLE),
                MovieProperties.DESC: tmdb_movie_info.get(TmdbMovieProperties.OWERVIEW)
            }
        else:
            raise rps.raise_for_status()