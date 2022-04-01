import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200

def test_api(client):
    response = client.get('/api/all')
    assert response.status_code == 200

def test_page_not_found(client):
    response = client.get('/not-found')
    assert response.status_code == 404

def test_homepage_content(client):
    response = client.get('/')
    assert b'Corporate tax information for year 2020' in response.data

def test_json_response(client):
    response = client.get('/api/all')
    assert response.headers['Content-Type'] == 'application/json'

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200

def test_about_page_content(client):
    response = client.get('/about')
    assert b'This is an amazing software' in response.data