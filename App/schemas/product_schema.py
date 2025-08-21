from pydantic import BaseModel, validator

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float

    @validator("price")
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be positive")
        return v
