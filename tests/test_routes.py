def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_about_page(client):
    response = client.get("/about")
    assert response.status_code == 200


def test_login_page(client):
    response = client.get("/login")
    assert response.status_code == 200


def test_register_page(client):
    response = client.get("/register")
    assert response.status_code == 200


def test_register_user(client):
    response = client.post(
        "/register",
        data={
            "username": "newuser",
            "email": "newuser@test.com",
            "password": "Password123!",
            "confirm_password": "Password123!",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200


def test_invalid_login(client):
    response = client.post(
        "/login", data={"email": "wrong@test.com", "password": "wrongpassword"}, follow_redirects=True
    )
    assert response.status_code == 200


def test_unauthorized_new_post(client):
    response = client.get("/post/new", follow_redirects=True)
    assert response.status_code == 200


def test_404_page(client):
    response = client.get("/nonexistent-page")
    assert response.status_code == 404
