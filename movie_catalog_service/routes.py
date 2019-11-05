from flask import Flask
from movie_catalog_service.configs import ServiceConfig


app = Flask(__name__)


@app.route('/catalog/<string:user_id>')
def get_movie_catalog(user_id):
    return f"get movie catalog with {user_id}"


if __name__ == '__main__':
    app.run(debug=ServiceConfig.DEBUG, port=ServiceConfig.PORT)
