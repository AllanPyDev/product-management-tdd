from datetime import datetime
from app.models.product_model import Product

class ProductUsecase:
    def __init__(self):
        self.products = []

    def create(self, product_data):
        try:
            product = Product(**product_data)
            self.products.append(product)
            return product
        except Exception as e:
            return {"error": str(e)}

    def update(self, product_id, update_data):
        product = next((p for p in self.products if p.id == product_id), None)
        if not product:
            return None
        for key, value in update_data.items():
            setattr(product, key, value)
        product.updated_at = update_data.get("updated_at", datetime.now())
        return product

    def filter_by_price(self, min_price, max_price):
        return [p for p in self.products if min_price < p.price < max_price]
