import pytest
from app.usecases.product_usecase import ProductUsecase

def test_create_product():
    uc = ProductUsecase()
    product = uc.create({"id": 1, "name": "Notebook", "price": 7000})
    assert product.name == "Notebook"

def test_update_product_not_found():
    uc = ProductUsecase()
    result = uc.update(99, {"name": "Novo"})
    assert result is None

def test_filter_price():
    uc = ProductUsecase()
    uc.create({"id": 1, "name": "Produto A", "price": 6000})
    uc.create({"id": 2, "name": "Produto B", "price": 9000})
    filtered = uc.filter_by_price(5000, 8000)
    assert len(filtered) == 1
    assert filtered[0].price == 6000
