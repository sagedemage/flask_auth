"""This test the homepage"""
import pytest
from flask import current_app


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


def test_registration_redirects_to_the_login_page(client):
    response = client.post("/register", data={"email": "test1000@gmail.com",
                                              "password": "test1000", "confirm": "test1000"})
    assert response.headers["Location"] == "/login"


def test_login_redirects_to_the_dashboard_page(client):
    response = client.post("/login", data={"email": "test1000@gmail.com", "password": "test1000"})
    assert response.headers["Location"] == "/dashboard"


def test_check_form_validates_email_and_password(client):
    """ Ensure that the login and registration page
    have email and password requirement"""

    # Register
    response = client.get("/register")
    # Bad email (Test 3)
    # -> check that email is required for the input element
    assert b"id=\"email\" name=\"email\" required type=\"email\"" in response.data
    # Bad password - does not meet criteria (Test 5)
    # check that password is required, maxlength is 35, and minlength is 6 for the input element
    assert b"id=\"password\" maxlength=\"35\" minlength=\"6\" " \
           b"name=\"password\" required type=\"password\"" in response.data

    # Login
    response = client.get("/login")
    # check that email is required for the input element
    assert b"id=\"email\" name=\"email\" required type=\"email\"" in response.data
    # check that password is required, maxlength is 35, and minlength is 6 for the input element
    assert b"id=\"password\" maxlength=\"35\" minlength=\"6\" " \
           b"name=\"password\" required type=\"password\"" in response.data


def test_registration_success(client):
    """ Registration """
    # Password Confirmation (Test 4)
    response = client.post("/register", data={"email": "test2000@gmail.com", "password": "test2000",
                                              "confirm": "test2001"}, follow_redirects=True)
    assert b"Passwords must match" in response.data

    # Successful Registration (Test 8)
    response = client.post("/register", data={"email": "test2000@gmail.com", "password": "test2000",
                                              "confirm": "test2000"}, follow_redirects=True)
    assert b"Congratulations, you are now a registered user!" in response.data

    # Already Registered (Test 6)
    response = client.post("/register", data={"email": "test2000@gmail.com", "password": "test2000",
                                              "confirm": "test2000"}, follow_redirects=True)
    assert b"Already Registered" in response.data


def test_login(client):
    """ Login """
    # This test does not work properly
    # Bad password (Test 1)
    response = client.post("/login", data={"email": "test2000@gmail.com", "password": "test9000"},
                           follow_redirects=True)
    assert b"Invalid email or password" in response.data
    # Bad email (Test 2)
    response = client.post("/login", data={"email": "test9000@gmail.com", "password": "test1000"},
                           follow_redirects=True)
    assert b"Invalid email or password" in response.data
    # Successful login (Test 7)
    response = client.post("/login", data={"email": "test2000@gmail.com", "password": "test2000"},
                           follow_redirects=True)
    assert b"Welcome to the dashboard" in response.data


def test_logout(client):
    """ Logout """
    response = client.get("/logout", follow_redirects=True)
    assert len(response.history) == 1
    assert response.request.path == "/login"


def test_deny_access_to_dashboard(client):
    """ Deny Access to the Dashboard """
    # denying access to the dashboard for users not logged in (Test 9)
    response = client.get("/dashboard", follow_redirects=True)
    assert b"Please log in to access this page." in response.data


def test_allow_access_to_dashboard(client):
    # allowing access to the dashboard for logged in users (Test 10)
    response = client.post("/login", data={"email": "test1000@gmail.com",
                                              "password": "test1000", "confirm": "test1000"})
    assert response.headers["Location"] == "/dashboard"
