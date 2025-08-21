from app.usecases.product_usecase import ProductUsecase

class ProductController:
    def __init__(self):
        self.usecase = ProductUsecase()

    def create_product(self, product_data):
        result = self.usecase.create(product_data)
        if "error" in result:
            return {"message": "Erro ao criar produto", "details": result["error"]}
        return {"message": "Produto criado com sucesso", "product": vars(result)}

    def update_product(self, product_id, update_data):
        result = self.usecase.update(product_id, update_data)
        if not result:
            return {"message": f"Produto {product_id} não encontrado"}
        return {"message": "Produto atualizado com sucesso", "product": vars(result)}

    def filter_products(self, min_price, max_price):
        products = self.usecase.filter_by_price(min_price, max_price)
        return [vars(p) for p in products]
