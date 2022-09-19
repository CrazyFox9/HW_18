from marshmallow import Schema, fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from setup_db import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    trailer = db.Column(db.Text())
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, ForeignKey("genre.id"))
    genre = relationship("Genre")
    director_id = db.Column(db.Integer, ForeignKey("director.id"))
    director = relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre_id = fields.Int()
    director_id = fields.Int()
