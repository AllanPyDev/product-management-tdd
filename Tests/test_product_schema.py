import pytest
from app.schemas.product_schema import ProductSchema
from pydantic import ValidationError

def test_product_schema_valid():
    product = ProductSchema(id=1, name="Notebook", price=6000)
    assert product.price == 6000

def test_product_schema_invalid_price():
    with pytest.raises(ValidationError):
        ProductSchema(id=2, name="Mouse", price=-10)
