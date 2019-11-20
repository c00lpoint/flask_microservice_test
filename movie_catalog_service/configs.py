class FlaskConfig:
    DEBUG = True


class ApplicationConfig:
    APP_NAME = 'movie-catalog-service'
    SERVICE_PORT = 5001


class EurekaServiceName:
    RATING_DATA = "RATING-DATA-SERVICE"
    MOVIE_DATA = 'MOVIE-DATA-SERVICE'
