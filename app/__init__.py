from flask import Flask
from app.model.book import db


def create_app():
    """
    app初始化
    """
    app = Flask(__name__)

    # 引入flask配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    # 初始化sqlalchemy
    db.init_app(app)
    db.create_all(app=app)

    # 注册蓝图
    register_blueprint(app)

    return app


def register_blueprint(app):
    """
    注册蓝图
    """
    from app.web import webBlueprint
    app.register_blueprint(webBlueprint)
    pass
