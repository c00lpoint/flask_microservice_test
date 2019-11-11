from rating_data_service import create_app
from rating_data_service.configs import ApplicationConfig

if __name__ == '__main__':
    app = create_app()
    app.run(port=ApplicationConfig.SERVICE_PORT)