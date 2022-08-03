from flask_restx import Namespace, Resource

from implemented import directors_schema, director_service, director_schema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        return directors_schema.dump(director_service.get_all()), 200


@director_ns.route('/<int:did>')
class DirectorViews(Resource):
    def get(self, did):
        return director_schema.dump(director_service.get_one(did)), 200
