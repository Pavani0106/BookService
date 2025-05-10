from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float
    is_rentable: bool
    is_available: bool
    category_id: Optional[int] = None
