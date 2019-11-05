from flask import Flask

from movie_data_service.configs import ServiceConfig

app = Flask(__name__)


@app.route('/movie/<int:movie_id>')
def get_movie(movie_id):
    return f"get movie with {movie_id}"


if __name__ == '__main__':
    app.run(debug=ServiceConfig.DEBUG, port=ServiceConfig.PORT)