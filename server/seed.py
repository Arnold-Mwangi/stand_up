from random import choice
from faker import Faker
from app import app
from models import db, Book, Genre, Author

fake = Faker()

with app.app_context():
    Book.query.delete()
    Genre.query.delete()
    Author.query.delete()

    authors = []
    for i in range(10):
        author = Author(name = fake.name())
        authors.append(author)

    db.session.add_all(authors)

    genres = []
    selected_genres = ["Fiction", "Mystery", "Science Fiction", "Fantasy", "Romance", "Thriller", "Non-Fiction", "Biography", "Self-Help", "History"]
    for i in range(10):
        genre = Genre(name = choice(selected_genres))
        genres.append(genre)
    db.session.add_all(genres)

    books=[]
    for n in range (50):
        title = fake.catch_phrase()
        author = choice(authors)
        genre = choice(genres)
        book = Book(title=title, author=author, genre = genre)
        books.append(book)
        db.session.add (book)
        
    db.session.commit()

