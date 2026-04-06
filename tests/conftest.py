import os
os.environ['SECRET_KEY'] = 'test-secret-key'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
os.environ['EMAIL_USER'] = 'test@test.com'
os.environ['EMAIL_PASS'] = 'testpass'

import pytest
from flaskblog import create_app, db
from flaskblog.models import User, Post

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'WTF_CSRF_ENABLED': False,
        'SECRET_KEY': 'test-secret-key',
        'MAIL_SUPPRESS_SEND': True,
        'MAIL_SERVER': 'localhost',
        'MAIL_PORT': 25,
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def test_user(app):
    with app.app_context():
        user = User(
            username='testuser',
            email='test@test.com',
            password='hashed_password'
        )
        db.session.add(user)
        db.session.commit()
        return user
