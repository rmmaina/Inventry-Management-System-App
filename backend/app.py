from flask import Flask 
from flask_cors import CORS
from config import Config
from extensions import db, migrate, jwt
from routes.product_routes import product_bp



app = Flask(__name__)
app.config.from_object(Config)
app.config["JWT_SECRET_KEY"] = "your-secret-key"
CORS(app)

@app.route("/")
def home():
    return {"message": "Inventory API is running"} 

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)
from routes import *
if __name__ == "__main__":
    app.run(debug=True)

from routes.auth_routes import auth_bp

app.register_blueprint(auth_bp, url_prefix="/api/auth")

app.register_blueprint(product_bp, url_prefix="/api")
