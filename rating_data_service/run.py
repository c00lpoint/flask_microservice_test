from rating_data_service import create_app
from rating_data_service.configs import ServiceConfig

if __name__ == '__main__':
    app = create_app(__name__)
    app.run(debug=ServiceConfig.DEBUG, port=ServiceConfig.PORT)