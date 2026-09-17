from flask import Flask, jsonify, request, redirect, render_template_string

app = Flask(__name__)

products = [
    {"id": 1, "name": "Cloud Backup", "price": 12.99},
    {"id": 2, "name": "Security Scanner", "price": 19.99},
    {"id": 3, "name": "Team Collaboration", "price": 9.99}
]

orders = []

PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>AppDirect Demo</title>
<style>
body {
    font-family: Arial;
    max-width: 900px;
    margin: 40px auto;
}
.product {
    border: 1px solid #ccc;
    padding: 15px;
    margin: 10px;
}
</style>
</head>

<body>

<h1>AppDirect Demo Marketplace</h1>
<h2>Monolithic Application on EC2</h2>

<h3>Products</h3>

{% for product in products %}
<div class="product">

<strong>{{ product.name }}</strong>
- ${{ product.price }}

<form method="POST" action="/order">

<input
type="hidden"
name="product_id"
value="{{ product.id }}">

<button type="submit">
Order
</button>

</form>

</div>
{% endfor %}

<h3>Orders</h3>

{% for order in orders %}
<p>
Order {{ order.id }}:
{{ order.product_name }}
</p>
{% endfor %}

</body>
</html>
"""

@app.route("/")
def home():

    return render_template_string(
        PAGE,
        products=products,
        orders=orders
    )


@app.post("/order")
def order():

    product_id = int(request.form["product_id"])

    product = next(
        p for p in products
        if p["id"] == product_id
    )

    orders.append({
        "id": len(orders) + 1,
        "product_name": product["name"]
    })

    return redirect("/")


@app.get("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
