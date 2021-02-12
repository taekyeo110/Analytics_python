import unittest
from flask_script import Manager
from app import blueprint
from app.main import create_app
from app.main.config.server_config import *
from app.main.routes.sample_router import sample


app = create_app(SERVER_ENV or 'development')
app.register_blueprint(blueprint, url_prefix='/doc')
app.register_blueprint(sample, url_prefix='/')
app.app_context().push()
manager = Manager(app)


@manager.command
def run():
    """
        서버 어플리케이션 실행 함수
        > python manage.py run
    """
    app.run(port=SERVER_PORT)


@manager.command
def unit_test():
    """
        유닛테스트 실행 함수
        > python manage.py unit_test
    """
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def py_test():
    """
        파이테스트 실행 함수
        > python manage.py py_test
    """
    os.system('pytest ./app/test')


if __name__ == '__main__':
    manager.run()
