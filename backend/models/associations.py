from extensions import db

user_products = db.Table(
    "user_products",

    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"))
)