from flask import Blueprint, current_app, request, jsonify
from .model import Book
from .serealizer import BookSchema

bp_books = Blueprint('books', __name__)


@bp_books.route('/', methods=['GET'])
def all():
    bs = BookSchema(many=True)
    result = Book.query.all()

    return bs.jsonify(result), 200

@bp_books.route('/<id>', methods=['GET'])
def search(id):
    bs = BookSchema(many=True)
    result = Book.query.filter(Book.id == id)

    return bs.jsonify(result), 200

@bp_books.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()

    return jsonify(f'Book of id {id} deleted!')

@bp_books.route('/update/<id>', methods=['POST'])
def update(id):
    bs = BookSchema()
    query = Book.query.filter(Book.id == id)
    query.update(request.json)
    current_app.db.session.commit()
    
    return bs.jsonify(query.first())

@bp_books.route('/create', methods=['POST'])
def create():
    bs = BookSchema()
    book = bs.load(request.json)
    current_app.db.session.add(book)
    current_app.db.session.commit()

    return bs.jsonify(book), 201
