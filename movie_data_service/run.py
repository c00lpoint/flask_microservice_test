from movie_data_service import create_app
from movie_data_service.configs import ApplicationConfig

if __name__ == '__main__':
    app = create_app(__name__)
    app.run(port=ApplicationConfig.SERVICE_PORT)