from flask import url_for


def test_get_route_did(app, client):
    with app.app_context():
        result = client.get(url_for('api.view_get_did'))
    assert 'hello' in result.text