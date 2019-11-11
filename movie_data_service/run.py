from movie_data_service.configs import ServiceConfig
from movie_data_service import create_app

if __name__ == '__main__':
    app = create_app(__name__)
    app.run()