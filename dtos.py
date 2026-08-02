
from pydantic import BaseModel


class ProductDTO(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    stock: int | None = None