from flask import jsonify, app

from app.api.bookapi import Book
from helper import is_isbn_or_key


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    q : 普通关键字 & isbn
    page : start & count
    """
    # isbn13 : 13个0到9的数字组成
    # isbn10 : 10个0到9的数字组成，含有一些'-'
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = Book.search_by_isbn(q)
    else:
        result = Book.search_by_keyword(q)

    # return json.dumps(result), 200, {'content-type':'application/json'}
    return jsonify(result)
