from flask import make_response

from app.web import webBlueprint


@webBlueprint.route('/login')
def login():
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html></html>', 200)
    response.headers = headers
    return response
