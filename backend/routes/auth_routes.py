from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    hashed_password = generate_password_hash(data["password"])

    user = User(
        username=data["username"],
        password_hash=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()

    if user and check_password_hash(user.password_hash, data["password"]):

        token = create_access_token(identity=user.id)

        return jsonify({
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username
            }
        })

    return jsonify({"error": "Invalid credentials"}), 401