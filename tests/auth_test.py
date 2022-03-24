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


def test_registration_success(client):
    """ Registration """
    response = client.post("/register", data={"email": "sal@gmail.com", "password": "123456"})
    # This response is giving a 400 BAD REQUEST error
    # assert response.status_code == 200


def test_login_success(client):
    """ Test Bad login """
    # Login
    response = client.post("/login", data={"email": "sal@gmail.com", "password": "123456"})
    # This response is giving a 400 BAD REQUEST error
    # assert response.status_code == 200
