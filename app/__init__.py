from flask_restx import Api
from flask import Blueprint

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='TK Server',
          version='1.0',
          description='데이터 엔지니어 서버'
          )
