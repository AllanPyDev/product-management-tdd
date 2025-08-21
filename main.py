from app.controllers.product_controller import ProductController

controller = ProductController()

# Criar produtos
controller.create_product({"id": 1, "name": "Notebook", "price": 6000})
controller.create_product({"id": 2, "name": "Mouse", "price": 3000})
controller.create_product({"id": 3, "name": "Monitor", "price": 7500})

# Atualizar produto
print(controller.update_product(1, {"price": 6500}))

# Filtrar produtos por preço
filtered = controller.filter_products(5000, 8000)
print("Produtos filtrados:", filtered)
