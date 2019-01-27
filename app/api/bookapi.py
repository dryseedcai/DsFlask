from app.utils.httputil import HTTP
from flask import current_app

class Book:
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        # print("url : " + url)
        result = HTTP.get(url, True)

        # dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PAGE_SIZE'], cls.calculate_start(page))
        # print("url : " + url)
        result = HTTP.get(url, True)
        return result

    @staticmethod
    def calculate_start(page):
        return current_app.config['PAGE_SIZE'] * (page - 1)
