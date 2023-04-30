import pytest
from telecom_carrier.app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,'SERVER_NAME': 'TELECOM_CARRIER_TEST'
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
