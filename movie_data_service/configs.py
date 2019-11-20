class FlaskConfig:
    DEBUG = True


class ApplicationConfig:
    APP_NAME = 'movie-data-service'
    SERVICE_PORT = 5002
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {name} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            }
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': './logs/service.log',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'movie_data_service': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': False
            },
        }
    }


class ExternalServiceUrls:
    TMDB_MOVIE_SEARCH_URL_FORMAT = 'https://api.themoviedb.org/3/movie/%d?api_key=02f3c125eb4f47a6f1daf49c91650b14'



