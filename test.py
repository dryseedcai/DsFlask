from flask import Flask

__author__ = "DS"

app = Flask(__name__)


@app.route('/Hello/')
def hello():
    return 'Hello, DS'


# 另一种路由注册方式
# def hello2():
#     return 'Hello2, DS'
# app.add_url_rule('/Hello2/', view_func=hello2)

# 引入flask配置文件
app.config.from_object('config')

app.run(debug=app.config['DEBUG'])
