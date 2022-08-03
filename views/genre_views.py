from flask_restx import Namespace, Resource

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresViews(Resource):
    def get(self):
        return 'общий список жанров работает', 200


@genre_ns.route('/<int:gid>')
class GenreViews(Resource):
    def get(self, gid):
        return 'gid работает', 200
