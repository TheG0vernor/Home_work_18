from marshmallow import Schema, fields

from setup_db import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def das_dict(self):
        return {'id': self.id,
                'name': self.name}


class GenreSchema(Schema):  # "Схема" жанров фильмов
    id = fields.Int(dump_only=True)
    name = fields.Str()
