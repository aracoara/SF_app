import json
from unittest.mock import patch

from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy
import pytest

from tennis_app.routes import app, submit_picks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db = SQLAlchemy(app)
            db.create_all()
        yield client

def test_submit_picks_with_valid_data(client: FlaskClient):
    # Mock the request data
    data = {
        'quartasFinal': {},
        'semiFinal': {},
        'final': {},
        'campeao': 'Player 1'
    }
    json_data = json.dumps(data)

    # Send a POST request to the submit_picks endpoint
    response = client.post('/submit_picks', data=json_data, content_type='application/json')

    # Assert the response
    assert response.status_code == 200
    assert response.json == {'message': 'Picks submitted successfully'}

    # Assert that the games were added to the database
    with app.app_context():
        db = SQLAlchemy(app)
        assert len(db.session.query(Game).all()) == 3

def test_submit_picks_with_invalid_data(client: FlaskClient):
    # Send a POST request to the submit_picks endpoint without any data
    response = client.post('/submit_picks')

    # Assert the response
    assert response.status_code == 400
    assert response.json == {'error': 'No data provided'}

def test_submit_picks_with_exception(client: FlaskClient):
    # Mock the request data
    data = {
        'quartasFinal': {},
        'semiFinal': {},
        'final': {},
        'campeao': 'Player 1'
    }
    json_data = json.dumps(data)

    # Mock an exception being raised during processing
    with patch('tennis_app.routes.process_round') as mock_process_round:
        mock_process_round.side_effect = Exception('An error occurred')

        # Send a POST request to the submit_picks endpoint
        response = client.post('/submit_picks', data=json_data, content_type='application/json')

    # Assert the response
    assert response.status_code == 500
    assert response.json == {'error': 'An error occurred'}