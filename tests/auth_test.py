"""This test the homepage"""
import pytest
from flask import g, session


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_auth_pages(client):
    """This makes the index page"""
    assert client.get("/dashboard").status_code == 302
    assert client.get("/register").status_code == 200
    assert client.get("/login").status_code == 200


@pytest.mark.parametrize(
    ("email", "password"),
    (("test1234@gmail.com", "test1234"),),
)
def test_registration_success(client, email, password):
    """ Registration """
    # This test does not work properly
    # The page keeps getting a 400 BAD REQUEST status code
    response = client.post("/register", data={"email": email, "password": password})
    assert response.status_code == 200


@pytest.mark.parametrize(
    ("email", "password"),
    (("test1234@gmail.com", "test1234"),),
)
def test_login_success(client, email, password):
    """ Login """
    # This test does not work properly
    # The page keeps getting a 400 BAD REQUEST status code
    response = client.post("/login", data={"email": email, "password": password})
    assert response.status_code == 200


def test_logout(client):
    """ Logout """
    response = client.get("/logout", follow_redirects=True)
    assert len(response.history) == 1
    assert response.request.path == "/login"


def test_deny_access_to_dashboard(client):
    """ Deny access to the Dashboard """
    # Ensure that the client does not have access
    # to the dashboard without logging in
    assert client.get("/dashboard").status_code == 302
