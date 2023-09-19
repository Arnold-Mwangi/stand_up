from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref = 'author',lazy=True)


    def __repr__(self):
        return f'<Author {self.name}>'

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    books = db.relationship('Book', backref='genre', lazy=True)

    def __repr__(self):
        return f'<Genre {self.name}>'


class Book(db.Model):
    __tablename__='books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)

    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable = False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'