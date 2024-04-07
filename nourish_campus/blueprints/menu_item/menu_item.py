from flask import Blueprint, render_template, request, redirect
from ...models.models import MenuItem, Restaurant
from ...extensions import db
from flask_login import current_user

menu_item_bp = Blueprint("menu_item", __name__, template_folder="templates")


@menu_item_bp.route("/menu_item/search?name=name&price=1", methods=['POST'])
def menu_item():
    # todo: add the following to all the admin posts
    # only admin can add a restaurant
    if not current_user.is_authenticated or not current_user.is_admin:
        return "Cannot add a restanrant because you are not an admin!"

    name = request.form['name']
    price = float(request.form['price'])
    calories = int(request.form['calories'])
    restaurant_id = int(request.form['restaurant_id'])
    new_menu_item = MenuItem(
        name=name, price=price, calories=calories, restaurant_id=restaurant_id)

    try:
        db.session.add(new_menu_item)
        db.session.commit()
        return redirect(f'/menu_item/{restaurant_id}')
    except:
        return 'There was an issue adding the menu item'


@menu_item_bp.route("/menu_item/<int:restaurant_id>", methods=['GET'])
def get_menu_item(restaurant_id):
    menu_items = MenuItem.query.filter_by(
        restaurant_id=restaurant_id).order_by(MenuItem.created_at).all()
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first()

    # first menu_index template is passed in, second is the var representing db query
    # menu_items contains all menu item queries, then used in template loop traversing the menu items
    return render_template('menu_index.html', menu_items=menu_items, restaurant=restaurant)
