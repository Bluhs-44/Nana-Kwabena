from flask import Flask, render_template, redirect, url_for, session, request
from uuid import uuid4

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

# Sample product data
PRODUCTS = {
    1: {"id": 1, "name": "Product One", "price": 29.99},
    2: {"id": 2, "name": "Product Two", "price": 49.99},
    3: {"id": 3, "name": "Product Three", "price": 19.99},
}

# Helpers

def get_cart():
    return session.setdefault("cart", {})

@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS.values())

@app.route("/product/<int:pid>")
def product_detail(pid):
    product = PRODUCTS.get(pid)
    if not product:
        return "Product not found", 404
    return render_template("product.html", product=product)

@app.route("/cart")
def view_cart():
    cart = get_cart()
    items = [PRODUCTS[int(pid)] | {"quantity": qty} for pid, qty in cart.items()]
    total = sum(item["price"] * item["quantity"] for item in items)
    return render_template("cart.html", items=items, total=total)

@app.route("/cart/add/<int:pid>", methods=["POST"])
def add_to_cart(pid):
    product = PRODUCTS.get(pid)
    if not product:
        return "Product not found", 404
    cart = get_cart()
    cart[str(pid)] = cart.get(str(pid), 0) + 1
    session.modified = True
    return redirect(url_for("view_cart"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = get_cart()
    if request.method == "POST":
        if not cart:
            return redirect(url_for("index"))
        # Here you would integrate with a real payment gateway
        order_id = str(uuid4())
        session.pop("cart", None)
        return render_template("confirmation.html", order_id=order_id)
    items = [PRODUCTS[int(pid)] | {"quantity": qty} for pid, qty in cart.items()]
    total = sum(item["price"] * item["quantity"] for item in items)
    return render_template("checkout.html", items=items, total=total)

if __name__ == "__main__":
    app.run(debug=True)
