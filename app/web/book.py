from flask import jsonify, request

from app.api.bookapi import Book
from app.forms.bookforms import BookSearchForm
from app.viewmodel.book import BookViewModel
from app.web import webBlueprint
from app.utils.helper import is_isbn_or_key


@webBlueprint.route('/book/search')
def search():
    """
    /book/search?q=9787501524044
    /book/search?q=我
    q : 普通关键字 & isbn
    page : start & count
    """

    # request参数获取
    # q = request.args['q']
    # page = request.args['page']

    # 参数验证
    form = BookSearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        # isbn13 : 13个0到9的数字组成
        # isbn10 : 10个0到9的数字组成，含有一些'-'
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = Book.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = Book.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)

        # return json.dumps(result), 200, {'content-type':'application/json'}
        return jsonify(result)
    else:
        return jsonify(form.errors)
