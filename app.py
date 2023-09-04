from flask import Flask, request

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
    return 'Hello World!'


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
    return 'Hello World!'


@app.route('/menu/<cat_name>', methods=['GET'])
def menu_category():  # put application's code here
    return 'Hello World!'


@app.route('/menu/<cat_name>/<dish>', methods=['GET'])
def menu_dish():  # put application's code here
    return 'Hello World!'


@app.route('/menu/<cat_name>/<dish>/review', methods=['GET', 'POST'])
def menu_dish_review():  # put application's code here
    return 'Hello World!'


@app.route('/menu/search', methods=['GET'])
def menu_search():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
