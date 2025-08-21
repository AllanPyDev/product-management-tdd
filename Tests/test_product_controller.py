import pytest
from app.controllers.product_controller import ProductController

def test_create_controller_success():
    controller = ProductController()
    response = controller.create_product({"id": 1, "name": "Notebook", "price": 6000})
    assert response["message"] == "Produto criado com sucesso"

def test_update_controller_not_found():
    controller = ProductController()
    response = controller.update_product(99, {"name": "Novo"})
    assert "não encontrado" in response["message"]

def test_filter_controller():
    controller = ProductController()
    controller.create_product({"id": 1, "name": "Produto A", "price": 6000})
    controller.create_product({"id": 2, "name": "Produto B", "price": 9000})
    filtered = controller.filter_products(5000, 8000)
    assert len(filtered) == 1
