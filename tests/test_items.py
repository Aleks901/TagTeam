"""Tests for the items controller."""

import pytest
from litestar.testing import TestClient
from app.main import app


@pytest.fixture(autouse=True)
def reset_items_db():
    """Reset the in-memory database before each test."""
    from app.controllers import items

    items.items_db.clear()
    items.next_id = 1
    yield
    items.items_db.clear()


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app=app)


def test_list_items_empty(client):
    """Test listing items when empty."""
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item(client):
    """Test creating a new item."""
    item_data = {"name": "Test Item", "description": "A test item", "price": 10.99}
    response = client.post("/items", json=item_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert data["price"] == item_data["price"]
    assert "id" in data


def test_get_item(client):
    """Test getting a specific item."""
    # First create an item
    item_data = {"name": "Test Item", "price": 10.99}
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]

    # Then get it
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == item_data["name"]


def test_update_item(client):
    """Test updating an item."""
    # First create an item
    item_data = {"name": "Test Item", "price": 10.99}
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]

    # Then update it
    updated_data = {"name": "Updated Item", "price": 20.99}
    response = client.put(f"/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_data["name"]
    assert data["price"] == updated_data["price"]


def test_delete_item(client):
    """Test deleting an item."""
    # First create an item
    item_data = {"name": "Test Item", "price": 10.99}
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]

    # Then delete it
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204

    # Verify it's gone
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404  # Should return Not Found
