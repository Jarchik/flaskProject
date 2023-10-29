from flask import Flask, request
import sqlite3
from db import get_db

app = Flask(__name__)



@app.route('/cart', methods=['GET', 'POST'])
def cart():  # put application's code here
    return 'Hello World!'


@app.route('/cart/order', methods=['POST'])
def cart_order():  # put application's code here
    return 'Hello World!'


@app.route('/cart/add', methods=['POST'])
def cart_add():  # put application's code here
    return 'Hello World!'


@app.route('/user', methods=['GET', 'POST', 'DELETE'])
def user():  # put application's code here
    return 'Hello World!'


@app.route('/user/register', methods=['POST'])
def user_register():  # put application's code here
    return 'Hello World!'


@app.route('/user/sign_in', methods=['POST'])
def user_sign_in():  # put application's code here
    return 'Hello World!'


@app.route('/user/logout', methods=['GET'])
def user_logout():  # put application's code here
    return 'Hello World!'


@app.route('/user/reset', methods=['POST'])
def user_reset():  # put application's code here
    return 'Hello World!'


@app.route('/user/history', methods=['GET'])
def user_history():  # put application's code here
    user = request.args.get('user')
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute(
        "SELECT o.*, od.*, d.Dish_name, d.Description FROM Orders as o "
        " LEFT JOIN ordered_dishes as od ON o.ID = od.order_id "
        " LEFT JOIN Dishes as d on d.ID = od.dish "
        " WHERE o.user = ?", (user,))
    rows = new_cur.fetchall()
    return rows


@app.route('/user/history/<id>', methods=['GET', 'POST', 'DELETE'])
def user_history_id():  # put application's code here
    return 'Hello World!'


@app.route('/user/address', methods=['GET', 'POST'])
def user_address():  # put application's code here
    return 'Hello World!'


@app.route('/user/address/<id>', methods=['GET', 'PUT', 'DELETE'])
def user_address_id():  # put application's code here
    return 'Hello World!'


@app.route('/menu', methods=['GET'])
def menu():  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute("SELECT * FROM Category")
    rows = new_cur.fetchall()
    return rows


@app.route('/menu/<cat>', methods=['GET'])
def menu_category(cat):  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute(
        "SELECT c.Name, d.* FROM Dishes as d "
        " LEFT JOIN Category as c on d.Category = c.ID "
        " WHERE c.name = ?", (cat,))
    rows = new_cur.fetchall()
    return rows


@app.route('/menu/<cat>/<dish>', methods=['GET'])
def menu_dish(cat, dish):  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute(
        "SELECT c.Name, d.* FROM Dishes AS d "
        " LEFT JOIN Category AS c ON d.Category = c.ID "
        " WHERE c.name = ? AND d.ID = ?", (cat, dish))
    rows = new_cur.fetchall()
    return rows


@app.route('/menu/<cat_name>/<dish>/review', methods=['GET', 'POST'])
def menu_dish_review():  # put application's code here
    return 'Hello World!'


@app.route('/menu/search', methods=['GET'])
def menu_search():  # put application's code here
    return 'Hello World!'


@app.route('/admin/users', methods=['GET'])
def admin_users():  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute("SELECT * FROM User")
    rows = new_cur.fetchall()
    return rows


@app.route('/admin/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def admin_users_id(id):  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute(
        "SELECT * FROM Users AS u "
        " WHERE u.ID = ?", (id,))
    rows = new_cur.fetchall()
    return rows


@app.route('/admin/users/<id>/address', methods=['GET', 'POST'])
def admin_users_address(id):  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute(
        "SELECT u.* FROM Users AS u "
        " LEFT JOIN Address AS a ON u.ID = a.User"
        " WHERE u.ID = ?", (id,))
    rows = new_cur.fetchall()
    return rows


@app.route('/admin/users/<user_id>/address/<address_id>', methods=['GET', 'PUT', 'DELETE'])
def admin_users_address_id(user_id, address_id):  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute(
        "SELECT u.* FROM Users AS u "
        " LEFT JOIN Address AS a ON u.ID = a.User"
        " WHERE u.ID = ? AND a.ID = ", (user_id, address_id))
    rows = new_cur.fetchall()
    return rows


@app.route('/admin/menu/categories', methods=['GET', 'POST'])
def admin_menu():  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute("SELECT * FROM Category")
    rows = new_cur.fetchall()
    return rows


@app.route('/admin/menu/categories/<cat>', methods=['GET', 'PUT', 'DELETE'])
def admin_menu_category(cat):  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute(
        "SELECT c.Name, d.* FROM Dishes as d "
        " LEFT JOIN Category as c on d.Category = c.ID "
        " WHERE c.name = ?", (cat,))
    rows = new_cur.fetchall()
    return rows


@app.route('/admin/menu/categories/<cat>/dishes/<dish>', methods=['GET', 'PUT', 'DELETE'])
def admin_menu_dish(cat, dish):  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute(
        "SELECT c.Name, d.* FROM Dishes AS d "
        " LEFT JOIN Category AS c ON d.Category = c.ID "
        " WHERE c.name = ? AND d.ID = ?", (cat, dish))
    rows = new_cur.fetchall()
    return rows


@app.route('/admin/orders', methods=['GET'])
def admin_orders():  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute(
        "SELECT o.*, od.*, d.Dish_name, d.Description FROM Orders as o "
        " LEFT JOIN ordered_dishes as od ON o.ID = od.order_id "
        " LEFT JOIN Dishes as d on d.ID = od.dish "
        )
    rows = new_cur.fetchall()
    return rows


@app.route('/admin/orders/<order_id>', methods=['GET', 'PUT', 'DELETE'])
def admin_order_id(order_id):  # put application's code here
    con = get_db()
    new_cur = con.cursor()
    new_cur.execute(
        "SELECT o.*, od.*, d.Dish_name, d.Description FROM Orders as o "
        " LEFT JOIN ordered_dishes as od ON o.ID = od.order_id "
        " LEFT JOIN Dishes as d on d.ID = od.dish "
        " WHERE o.ID = ?", (order_id,))
    rows = new_cur.fetchall()
    return rows


if __name__ == '__main__':
    app.run()
