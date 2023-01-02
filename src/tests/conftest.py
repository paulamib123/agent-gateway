import pytest
from flask import Flask
from unittest.mock import MagicMock

from src.routes.routes import registerRoutes

@pytest.fixture
def app(scope = "session"):
    app = Flask(__name__)
    app.config["TESTING"] = True
    session = MagicMock()
    registerRoutes(app, session)
    return app


@pytest.fixture
def client(app, scope = "session"):
    return app.test_client()
