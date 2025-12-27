
from src.models.products_model import Products

class ProductsRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_by_id(self, product_id: int):
        return self.db.query(Products).filter(Products.id == product_id).first()

    def list_all(self):
        return self.db.query(Products).all()

    def create(self, new_product: Products):
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)

        return new_product

    def update(self, product: Products):
        self.db.commit()
        self.db.refresh(product)

        return product

    def delete(self, product: Products):
        self.db.delete(product)
        self.db.commit()