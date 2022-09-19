from flask import request
from flask_restx import Namespace, Resource

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    movies_schema = MovieSchema(many=True)

    def get(self):
        all_movies = movie_service.get_all(**request.args)
        return self.movies_schema.dump(all_movies), 200

    def post(self):
        movie_service.create(request.json)

        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    movie_schema = MovieSchema()

    def get(self, mid):
        return self.movie_schema.dump(movie_service.get_one(mid)), 200

    def patch(self, mid):
        return self.movie_schema.dump(movie_service.update_partial(mid, request.json)), 200

    def put(self, mid):
        return self.movie_schema.dump(movie_service.update(mid, request.json)), 200

    def delete(self, mid):
        movie_service.delete(mid)

        return "", 204
