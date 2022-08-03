from flask import request
from flask_restx import Namespace, Resource

from implemented import movie_service, movies_schema, movie_schema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesViews(Resource):
    def get(self):
        movies_service = movie_service.get_all()
        if request.args.get('director_id'):
            movies_service = movie_service.get_by_director(request.args.get('director_id'))
        if request.args.get('genre_id'):
            movies_service = movie_service.get_by_genre(request.args.get('genre_id'))
        if request.args.get('year'):
            movies_service = movie_service.get_by_year(request.args.get('year'))
        return movies_schema.dump(movies_service), 200

    def post(self):
        movie_service.post_create(request.json)
        return "Фильм успешно добавлен", 201


@movie_ns.route('/<int:mid>')
class MovieViews(Resource):
    def get(self, mid):
        return movie_schema.dump(movie_service.get_one(mid)), 200

    def put(self, mid):
        movie_schema.dump(movie_service.put_update(request.json))
        return "", 204

    def patch(self, mid):
        movie_schema.dump(movie_service.patch_update(request.json))
        return "", 204

    def delete(self, mid):
        movie_schema.dump(movie_service.delete(mid))
        return "", 204
