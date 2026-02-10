"""Item model definition."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Item:
    """Item data model."""

    name: str
    description: Optional[str] = None
    price: float = 0.0
    id: Optional[int] = None
