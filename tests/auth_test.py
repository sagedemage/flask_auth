"""This test the homepage"""
import pytest
from flask import request

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
    ("email", "password", "confirm", "route"),
    (
        # Already Registered
        ("test1000@gmail.com", "test1000", "test1000", "/register"),
        # Bad Password
        ("test3000@gmail.com", "test3000", "test4000", "/register"),
        # Successful Registration
        ("test1235@gmail.com", "test1235", "test1235", "/login"),

    ),
)
def test_registration_success(client, email, password, confirm, route):
    """ Registration """
    # This test does not work properly
    response = client.post("/register", data={"email": email, "password": password, "confirm": confirm},
                           follow_redirects=True)
    assert response.request.path == route


@pytest.mark.parametrize(
    ("email", "password", "route"),
    (
        # bad password
        ("test1000@gmail.com", "test9000", "/login"),
        # bad email
        ("test9191@gmail.com", "test1000", "/login"),
        # successful login
        ("test1000@gmail.com", "test1000", "/dashboard"),
    ),
)
def test_login(client, email, password, route):
    """ Login """
    # This test does not work properly
    response = client.post("/login", data={"email": email, "password": password}, follow_redirects=True)
    assert response.request.path == route


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
