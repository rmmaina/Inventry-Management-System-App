#Add Blueprint
from flask import Blueprint, request, jsonify
from extensions import db
from models.product import Product
from flask_jwt_extended import jwt_required

product_bp = Blueprint("products", __name__)

#CREATE PRODUCT

@product_bp.route("/products", methods=["POST"])
@jwt_required()
def create_product():
    data = request.get_json()

    product = Product(
        name=data["name"],
        quantity=data["quantity"],
        category_id=data["category_id"]
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product created"})

#GET ALL PRODUCTS
@product_bp.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()

    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "quantity": p.quantity
        }
        for p in products
    ])

#UPDATE PRODUCT
@product_bp.route("/products/<int:id>", methods=["PATCH"])
@jwt_required()
def update_product(id):
    product = Product.query.get(id)
    data = request.get_json()

    product.name = data.get("name", product.name)
    product.quantity = data.get("quantity", product.quantity)

    db.session.commit()

    return jsonify({"message": "Product updated"})

#DELETE PRODUCT
@product_bp.route("/products/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_product(id):
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted"})

