from flask import Flask, make_response

__author__ = "DS"

app = Flask(__name__)


@app.route('/Hello/')
def hello():
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html></html>', 404)
    response.headers = headers
    return response


# 另一种路由注册方式
def hello2():
    return 'Hello2, DS'


app.add_url_rule('/Hello2/', view_func=hello2)


# make_response
@app.route('/Hello3/')
def hello3():
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.baidu.com'
    }
    response = make_response('<html></html>', 301)
    response.headers = headers
    return response


# 引入flask配置文件
app.config.from_object('config')

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
