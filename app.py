from flask import Flask, render_template, request, redirect, session, url_for
from flask import jsonify
from database.menu import (
    get_all_menu_items,
    add_menu_item,
    get_special_dishes,
    get_menu_item,
    update_menu_item,
    delete_menu_item,
    get_total_menu_items
)
from database.orders import (
    save_order,
    get_all_orders,
    update_order_status,
    get_total_orders,
    get_total_sales,
    get_order,
    get_order_items,
    delete_order,
    get_order_status_counts,
    get_weekly_sales,
    get_order_by_id
)
from database.reservations import (
    save_reservation,
    get_all_reservations,
    delete_reservation,
    get_total_reservations,
    update_reservation_status
)
from database.admin import (
    check_admin,
    create_default_admin
)

from database.table import (
    get_all_tables,
    get_table,
    update_table_status,
    get_table_stats,
    add_table,
    delete_table
)

from flask import send_file
from datetime import datetime

from flask import flash
import re


app = Flask(__name__)
app.secret_key = "varhadi_virasat_secret"

create_default_admin()

@app.route("/")
def home():

    special_dishes = get_special_dishes()

    return render_template(
        "/index.html",
        special_dishes=special_dishes
    )

@app.route("/menu")
def menu():

    menu_items = get_all_menu_items()

    return render_template(
        "/menu.html",
        menu_items=menu_items
    )

@app.route("/reservation")
def reservation():
    return render_template("/reservation.html")

@app.route("/save_reservation", methods=["POST"])
def save_reservation_route():

    name = request.form["name"]

    phone = request.form["phone"]

    reservation_date = request.form["reservation_date"]

    reservation_time = request.form["reservation_time"]

    guests = request.form["guests"]

    save_reservation(
        name,
        phone,
        reservation_date,
        reservation_time,
        guests
    )

    return redirect("/reservation_success")


@app.route("/cart")
def cart():

    cart_items = session.get("cart", [])

    subtotal = 0

    for item in cart_items:

        try:
            price = float(item["price"])
        except:
            price = 0

        subtotal += price * item["quantity"]

    gst = round(subtotal * 0.05, 2)

    grand_total = subtotal + gst

    return render_template(
        "/cart.html",
        cart_items=cart_items,
        subtotal=subtotal,
        gst=gst,
        grand_total=grand_total
    )

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():

    data = request.get_json()

    dish_name = data["dish_name"]

    price = float(data["price"])

    image = data["image"]

    cart = session.get("cart", [])

    for item in cart:

        if item["dish_name"] == dish_name:

            item["quantity"] += 1

            session["cart"] = cart

            return jsonify({

                "success": True,

                "cart_count": len(cart)

            })

    cart.append({

        "dish_name": dish_name,

        "price": price,

        "image": image,

        "quantity": 1

    })

    session["cart"] = cart

    return jsonify({

        "success": True,

        "cart_count": len(cart)

    })


@app.route("/increase_quantity", methods=["POST"])
def increase_quantity():

    dish_name = request.form["dish_name"]

    cart = session.get("cart", [])

    for item in cart:

        if item["dish_name"] == dish_name:

            item["quantity"] += 1

            break

    session["cart"] = cart

    return redirect("/cart")

@app.route("/decrease_quantity", methods=["POST"])
def decrease_quantity():

    dish_name = request.form["dish_name"]

    cart = session.get("cart", [])

    for item in cart:

        if item["dish_name"] == dish_name:

            if item["quantity"] > 1:

                item["quantity"] -= 1

            else:

                cart.remove(item)

            break

    session["cart"] = cart

    return redirect("/cart")

@app.route("/remove_item", methods=["POST"])
def remove_item():

    dish_name = request.form["dish_name"]

    cart = session.get("cart", [])

    cart = [

        item

        for item in cart

        if item["dish_name"] != dish_name

    ]

    session["cart"] = cart

    return redirect("/cart")


@app.route("/orders")
def orders():

    if "admin" not in session:
        return redirect("/login")

    orders = get_all_orders()

    return render_template(
        "orders.html",
        orders=orders
    )


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        admin = check_admin(username, password)

        if admin:

            session["admin"] = username

            return redirect("/admin")

        return render_template(
            "login.html",
            error="Invalid username or password."
        )

    return render_template("login.html")

@app.route("/admin")
def admin():

    if "admin" not in session:
        return redirect("/login")

    orders = get_all_orders()

    total_orders = get_total_orders()

    total_sales = get_total_sales()

    total_menu_items = get_total_menu_items()

    total_reservations = get_total_reservations()

    return render_template(

        "admin.html",

        orders=orders,

        total_orders=total_orders,

        total_sales=total_sales,

        total_menu_items=total_menu_items,

        total_reservations=total_reservations

    )

@app.route("/dashboard")
def dashboard():

    if "admin" not in session:
        return redirect("/login")

    orders = get_all_orders()

    total_orders = get_total_orders()

    total_sales = get_total_sales()

    total_menu_items = get_total_menu_items()

    total_reservations = get_total_reservations()

    status_counts = get_order_status_counts()

    weekly_sales = get_weekly_sales()

    return render_template(

        "dashboard.html",

        orders=orders,

        total_orders=total_orders,

        total_sales=total_sales,

        total_menu_items=total_menu_items,

        total_reservations=total_reservations,

        status_counts=status_counts,

        weekly_sales=weekly_sales

    )

@app.route("/manage_reservations")
def manage_reservations():

    if "admin" not in session:
        return redirect("/login")

    reservations = get_all_reservations()

    return render_template(
        "manage_reservations.html",
        reservations=reservations
    )

@app.route("/delete_reservation/<int:reservation_id>")
def delete_reservation_route(reservation_id):

    if "admin" not in session:
        return redirect("/login")

    delete_reservation(reservation_id)

    return redirect("/manage_reservations")

@app.route("/logout")
def logout():

    session.pop("admin", None)

    return redirect("/")

@app.route("/update_status", methods=["POST"])
def update_status():

    order_id = request.form["order_id"]

    status = request.form["status"]

    update_order_status(order_id, status)

    return redirect("/admin")

@app.route("/edit_dish/<int:item_id>")
def edit_dish(item_id):

    if "admin" not in session:
        return redirect("/login")

    item = get_menu_item(item_id)

    if item is None:
        return "Dish not found", 404

    return render_template(
        "edit_dish.html",
        item=item
    )

@app.route("/delete_order/<int:order_id>")
def delete_order_route(order_id):

    if "admin" not in session:
        return redirect("/login")

    delete_order(order_id)

    return redirect("/admin")

@app.route("/checkout")
def checkout():

    return render_template("checkout.html")


@app.route("/place_order", methods=["POST"])
def place_order():

    order_type = request.form["order_type"]

    payment_method = request.form["payment_method"]

    customer_name = request.form["customer_name"]
    phone = request.form["phone"]

    customer_name = customer_name.strip()
    phone = phone.strip()

    if not re.fullmatch(r"[A-Za-z ]{2,40}", customer_name):
        flash("Customer name must contain only letters and spaces (2-40 characters).")
        return redirect(url_for("checkout"))

    if not re.fullmatch(r"[6-9]\d{9}", phone):
        flash("Please enter a valid 10-digit Indian mobile number.")
        return redirect(url_for("checkout"))

    table_number = session.get("table_number")

    if not table_number:
        table_number = request.form.get("table_number")

    if order_type == "Takeaway":
        table_number = None

    cart_items = session.get("cart", [])

    if not cart_items:
        flash("Your cart is empty. Please add at least one item before placing an order.")
        return redirect(url_for("cart"))

    total = 0

    for item in cart_items:
        total += float(item["price"]) * item["quantity"]

    order_id = save_order(
        customer_name,
        phone,
        order_type,
        payment_method,  
        table_number,
        total,
        cart_items
    )

    session["cart"] = []

    return redirect(url_for(
        "success",
        order_id=order_id
    ))

@app.route("/success")
def success():

    order_id = request.args.get("order_id")

    return render_template(
        "order_success.html",
        order_id=order_id
    )

@app.route("/reservation_success")
def reservation_success():

    return render_template("reservation_success.html")

@app.route("/manage_menu")
def manage_menu():

    if "admin" not in session:
        return redirect("/login")

    menu_items = get_all_menu_items()

    return render_template(
        "manage_menu.html",
        menu_items=menu_items
    )

@app.route("/manage_tables")
def manage_tables():

    if "admin" not in session:
        return redirect("/login")

    tables = get_all_tables()

    stats = get_table_stats()

    return render_template(
        "manage_tables.html",
        tables=tables,
        stats=stats
    )

@app.route("/add_dish")
def add_dish():

    return render_template("add_dish.html")


@app.route("/save_dish", methods=["POST"])
def save_dish():

    dish_name = request.form["dish_name"]

    category = request.form["category"]

    price = request.form["price"]

    description = request.form["description"]

    image = request.form["image"]

    add_menu_item(
        dish_name,
        category,
        price,
        image,
        description
    )

    return redirect("/manage_menu")

@app.route("/delete_dish/<int:item_id>")
def delete_dish(item_id):

    delete_menu_item(item_id)

    return redirect("/manage_menu")

@app.route("/update_dish/<int:item_id>", methods=["POST"])
def update_dish(item_id):

    dish_name = request.form["dish_name"]

    category = request.form["category"]

    price = request.form["price"]

    description = request.form["description"]

    image = request.form["image"]

    update_menu_item(
        item_id,
        dish_name,
        category,
        price,
        image,
        description
    )

    return redirect("/manage_menu")

@app.route("/invoice/<int:order_id>")
def invoice(order_id):

    order = get_order(order_id)
    items = get_order_items(order_id)

    current_date = datetime.now().strftime("%d-%m-%Y")
    current_time = datetime.now().strftime("%I:%M %p")

    ITEMS_PER_PAGE = 12

    pages = []

    for i in range(0, len(items), ITEMS_PER_PAGE):
        pages.append(items[i:i + ITEMS_PER_PAGE])

    return render_template(
        "invoice.html",
        order=order,
        items=items,
        pages=pages,
        current_date=current_date,
        current_time=current_time
    )

@app.route("/order_details/<int:order_id>")
def order_details(order_id):

    if "admin" not in session:
        return redirect("/login")

    order = get_order(order_id)

    items = get_order_items(order_id)

    return render_template(
        "order_details.html",
        order=order,
        items=items
    )

@app.route("/print_invoice/<int:order_id>")
def print_invoice(order_id):

    order = get_order(order_id)
    items = get_order_items(order_id)

    current_date = datetime.now().strftime("%d-%m-%Y")
    current_time = datetime.now().strftime("%I:%M %p")

    return render_template(
        "print_invoice.html",
        order=order,
        items=items,
        current_date=current_date,
        current_time=current_time,
        auto_print=True
    )


@app.route("/confirm_reservation/<int:reservation_id>")
def confirm_reservation(reservation_id):

    if "admin" not in session:
        return redirect("/login")

    update_reservation_status(
        reservation_id,
        "Confirmed"
    )

    return redirect("/manage_reservations")


@app.route("/dining_reservation/<int:reservation_id>")
def dining_reservation(reservation_id):

    if "admin" not in session:
        return redirect("/login")

    update_reservation_status(
        reservation_id,
        "Dining"
    )

    return redirect("/manage_reservations")


@app.route("/complete_reservation/<int:reservation_id>")
def complete_reservation(reservation_id):

    if "admin" not in session:
        return redirect("/login")

    update_reservation_status(
        reservation_id,
        "Completed"
    )

    return redirect("/manage_reservations")


@app.route("/track_order/<int:order_id>")
def track_order(order_id):

    order = get_order_by_id(order_id)

    if order is None:
        return "Order Not Found"

    return render_template(
        "track_order.html",
        order=order
    )


@app.route("/table/<int:table_number>")
def table_menu(table_number):

    session["table_number"] = table_number

    menu = get_all_menu_items()

    return render_template(
        "index.html",
        menu=menu,
        table_number=table_number
    )

@app.route("/add_table", methods=["GET","POST"])
def add_table_page():

    if "admin" not in session:
        return redirect("/login")

    if request.method == "POST":

        table_number = request.form["table_number"]

        area = request.form["area"]

        position = request.form["position"]

        add_table(
            int(table_number),
            area,
            position
        )

        flash("New Table Added Successfully!")

        return redirect("/manage_tables")

    return render_template("add_table.html")

@app.route("/delete_table/<int:table_id>")
def delete_table_route(table_id):

    if "admin" not in session:
        return redirect("/login")

    delete_table(table_id)

    flash("Table deleted successfully!")

    return redirect("/manage_tables")

@app.route("/view_qr/<int:table_id>")
def view_qr(table_id):

    table = get_table(table_id)

    return render_template(
        "view_qr.html",
        table=table
    )

@app.route("/download_qr/<int:table_id>")
def download_qr(table_id):

    table = get_table(table_id)

    return render_template(
        "download_qr.html",
        table=table
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )











