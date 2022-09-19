from flask_restx import Namespace, Resource

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    Genres_schema = GenreSchema(many=True)

    def get(self):
        return self.Genres_schema.dump(genre_service.get_all()), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    Genre_schema = GenreSchema()

    def get(self, gid):
        return self.Genre_schema.dump(genre_service.get_one(gid)), 200
