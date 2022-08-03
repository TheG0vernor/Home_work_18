from flask_restx import Namespace, Resource

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesViews(Resource):
    def get(self):
        return 'общий список фильмов работает', 200

    def post(self):
        return 'фильм создаётся', 201


@movie_ns.route('/<int:mid>')
class MovieViews(Resource):
    def get(self, mid):
        return 'mid работает', 200

    def put(self, mid):
        return 'mid обновляется', 204

    def delete(self, mid):
        return 'mid удаляется', 204
