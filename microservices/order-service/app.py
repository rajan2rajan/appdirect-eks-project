
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "order-service",
        "message": "Order Service is running"
    })

@app.route("/api/orders")
def orders():
    return jsonify([
        {"id": 101, "product": "Laptop", "status": "Completed"},
        {"id": 102, "product": "Phone", "status": "Processing"}
    ])

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "order-service"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
