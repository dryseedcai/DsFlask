from flask import Flask

app = Flask(__name__)

# 引入flask配置文件
app.config.from_object('config')

if __name__ == '__main__':
    app.run(debug=True)
