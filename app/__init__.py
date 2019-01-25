from flask import Flask


def create_app():
    """
    app初始化
    """
    app = Flask(__name__)

    # 引入flask配置文件
    app.config.from_object('config')

    # 注册蓝图
    register_blueprint(app)

    return app


def register_blueprint(app):
    """
    注册蓝图
    """
    from app.web.book import web
    app.register_blueprint(web)
    pass
