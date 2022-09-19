from flask_restx import Namespace, Resource

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    directors_schema = DirectorSchema(many=True)

    def get(self):
        return self.directors_schema.dump(director_service.get_all()), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    director_schema = DirectorSchema()

    def get(self, did):
        return self.director_schema.dump(director_service.get_one(did)), 200
