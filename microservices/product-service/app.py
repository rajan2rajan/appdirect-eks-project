
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "product-service",
        "message": "Product Service is running"
    })

@app.route("/api/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 1200},
        {"id": 2, "name": "Phone", "price": 800},
        {"id": 3, "name": "Headphones", "price": 150}
    ])

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "product-service"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
