from datetime import datetime

class Product:
    def __init__(self, id, name, price, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.price = price
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
