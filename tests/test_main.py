"""Tests for the main application."""
import pytest
from litestar.testing import TestClient
from app.main import app


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app=app)


def test_index(client):
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Welcome to Litestar!"


def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
