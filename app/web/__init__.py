# 创建蓝图
from flask import Blueprint

webBlueprint = Blueprint('web', __name__)

# 导入进来，才会去进行路由注册
from app.web import book
from app.web import user