from flaskblog import db
from flaskblog.models import Post, User


def test_user_creation(app):
    with app.app_context():
        user = User(username="omar", email="omar@test.com", password="hashedpass")
        db.session.add(user)
        db.session.commit()
        assert user.id is not None
        assert user.username == "omar"
        assert user.email == "omar@test.com"


def test_user_default_image(app):
    with app.app_context():
        user = User(username="omar2", email="omar2@test.com", password="hashedpass")
        db.session.add(user)
        db.session.commit()
        assert user.image_file == "default.jpg"


def test_post_creation(app):
    with app.app_context():
        user = User(username="postuser", email="postuser@test.com", password="hashedpass")
        db.session.add(user)
        db.session.commit()

        post = Post(title="My Post", content="My Content", user_id=user.id)
        db.session.add(post)
        db.session.commit()
        assert post.id is not None
        assert post.title == "My Post"
        assert post.content == "My Content"


def test_user_post_relationship(app):
    with app.app_context():
        user = User(username="reluser", email="reluser@test.com", password="hashedpass")
        db.session.add(user)
        db.session.commit()

        post = Post(title="Rel Post", content="Rel Content", user_id=user.id)
        db.session.add(post)
        db.session.commit()

        assert len(user.posts) == 1
        assert user.posts[0].title == "Rel Post"
