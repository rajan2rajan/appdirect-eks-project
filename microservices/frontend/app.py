
from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://product-service:5000/api/products"
)

ORDER_SERVICE_URL = os.getenv(
    "ORDER_SERVICE_URL",
    "http://order-service:5000/api/orders"
)

@app.route("/")
def home():
    try:
        products = requests.get(PRODUCT_SERVICE_URL, timeout=5).json()
    except Exception:
        products = {"error": "Product service unavailable"}

    try:
        orders = requests.get(ORDER_SERVICE_URL, timeout=5).json()
    except Exception:
        orders = {"error": "Order service unavailable"}

    return jsonify({
        "application": "AppDirect Microservices on Amazon EKS",
        "products": products,
        "orders": orders
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "frontend"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
