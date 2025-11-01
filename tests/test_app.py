import pytest
from awsengine import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Check if home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"<form" in response.data  # checks if form exists


def test_prediction(client):
    """Check if /predict works properly"""
    sample_input = {'review': 'This movie was absolutely amazing!'}
    response = client.post('/predict', data=sample_input)
    assert response.status_code == 200
    assert b'Positive' in response.data or b'Negative' in response.data
