from flask import Flask

from rating_data_service.configs import ServiceConfig

app = Flask(__name__)


@app.route('/rating/<int:movie_id>')
def get_rating(movie_id):
    return f"get rating with {movie_id}"


if __name__ == '__main__':
    app.run(debug=ServiceConfig.DEBUG, port=ServiceConfig.PORT)