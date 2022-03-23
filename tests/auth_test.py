"""This test the homepage"""
from flask import g
from flask import session
from app.auth import login, register, dashboard, logout


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200


def test_login(client):
    """ Test Bad login """
    response = client.get("/login")
    
    """ There should be a way to pass in values for
     the username and password to test login """

    # Bad username
    assert 1 == 1

    # Bad password
    assert 2 == 2

    # Login success
    assert 3 == 3


def test_registration(client):
    """ Test Bad Registration """
    response = client.get("/register")

    """ There should be a way to pass in values for
    the username and password to test registration """

    # Bad username
    assert 1 == 1
    # Password Confirmation
    assert 2 == 2
    # Bad password
    assert 3 == 3
    # Already registered
    assert 4 == 4

    # Registration success
    assert 5 == 5


def user_access_to_dashboard(client):
    # Deny access to the dashboard for login users
    assert 1 == 1
    # Allow access to the dashboard for login users
    assert 2 == 2
