import pytest
from fastapi.testclient import TestClient

from fast_api_crud.app import app


@pytest.fixture
def client():
    return TestClient(app)
