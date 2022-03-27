"""This test the homepage"""
import pytest
from flask import request, redirect, session
from flask import g
from flask_login import current_user, login_user
from app.db.models import User


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


def test_registration_works(client):
    response = client.post("/register", data={"email": "test1000@gmail.com",
                                              "password": "test1000", "confirm": "test1000"})
    assert response.headers["Location"] == "http://localhost/login"


def test_registration_success(client):
    """ Registration """
    # This test does not work properly
    # Already Registered
    response = client.post("/register", data={"email": "test1000@gmail.com", "password": "test1000",
                                              "confirm": "test1000"}, follow_redirects=True)
    assert b"Already Registered" in response.data
    # Skip bad Email
    # Bad password
    response = client.post("/register", data={"email": "test2000@gmail.com", "password": "test2000",
                                              "confirm": "test2001"}, follow_redirects=True)
    assert b"Passwords must match" in response.data
    # Successful Registration (Good password)
    response = client.post("/register", data={"email": "test2000@gmail.com", "password": "test2000",
                                              "confirm": "test2000"}, follow_redirects=True)
    assert b"Congratulations, you are now a registered user!" in response.data


def test_login(client):
    """ Login """
    # This test does not work properly
    # Bad password
    response = client.post("/login", data={"email": "test1000@gmail.com", "password": "test9000"},
                           follow_redirects=True)
    assert b"Invalid email or password" in response.data
    # Bad email
    response = client.post("/login", data={"email": "test9000@gmail.com", "password": "test1000"},
                           follow_redirects=True)
    assert b"Invalid email or password" in response.data
    # Successful login
    response = client.post("/login", data={"email": "test1000@gmail.com", "password": "test1000"},
                           follow_redirects=True)
    assert b"Welcome to the dashboard" in response.data


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
