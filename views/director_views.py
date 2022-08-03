from flask_restx import Namespace, Resource

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        return 'общий список директоров работает', 200


@director_ns.route('/<int:did>')
class DirectorViews(Resource):
    def get(self, did):
        return 'did работает', 200
