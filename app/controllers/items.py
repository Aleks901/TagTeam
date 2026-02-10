"""Items controller for CRUD operations."""
from litestar import Controller, get, post, put, delete
from litestar.status_codes import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from app.models.item import Item


# In-memory storage for demo purposes
items_db: dict[int, Item] = {}
next_id = 1


class ItemController(Controller):
    """Item management endpoints."""

    path = "/items"

    @get()
    async def list_items(self) -> list[Item]:
        """Get all items."""
        return list(items_db.values())

    @get("/{item_id:int}")
    async def get_item(self, item_id: int) -> Item:
        """Get a specific item by ID."""
        if item_id not in items_db:
            raise ValueError(f"Item {item_id} not found")
        return items_db[item_id]

    @post(status_code=HTTP_201_CREATED)
    async def create_item(self, data: Item) -> Item:
        """Create a new item."""
        global next_id
        data.id = next_id
        items_db[next_id] = data
        next_id += 1
        return data

    @put("/{item_id:int}")
    async def update_item(self, item_id: int, data: Item) -> Item:
        """Update an existing item."""
        if item_id not in items_db:
            raise ValueError(f"Item {item_id} not found")
        data.id = item_id
        items_db[item_id] = data
        return data

    @delete("/{item_id:int}", status_code=HTTP_204_NO_CONTENT)
    async def delete_item(self, item_id: int) -> None:
        """Delete an item."""
        if item_id not in items_db:
            raise ValueError(f"Item {item_id} not found")
        del items_db[item_id]
