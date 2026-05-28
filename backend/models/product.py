from extensions import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(80), nullable=False)

    qty = db.Column(db.Integer, nullable=False)

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    users = db.relationship(
        "User",
        secondary="user_products",
        back_populates="products"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "qty": self.qty,
            "category_id": self.category_id
        }

 