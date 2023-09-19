from models import db, Book, Genre, Author
from flask_migrate import Migrate
from flask import Flask , make_response, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return f'<h1>Welcome to our book store</h1>'

@app.route('/success/<int:book_id>')
def success(book_id):
    book = Book.query.get(book_id)
    if book:
        return render_template('success.html', book = book)
    else:
        return render_template('notsuccess.html'), 404

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author_id = request.form['author_id']
        genre_id = request.form['genre_id']

        book = Book(title=title, author_id=author_id, genre_id=genre_id)
        db.session.add(book)
        db.session.commit()

        last_book_id = book.id

        return redirect(url_for('success', book_id = last_book_id))  
    else:
        return render_template('add_book.html')


if __name__ == '__main__':
    app.run(port=5555, debug=True)