from flask import Blueprint, render_template, request, redirect
from ...models.models import MenuItem
from ...extensions import db

menu_item_bp = Blueprint("menu_item", __name__, template_folder="templates")

@menu_item_bp.route("/menu_item", methods=['POST', 'GET'])
def menu_item():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        calories = int(request.form['calories'])
        restaurant_id = int(request.form['restaurant_id'])
        new_menu_item = MenuItem(
            name=name, price=price, calories=calories, restaurant_id=restaurant_id)

        try:
            db.session.add(new_menu_item)
            db.session.commit()
            return redirect('/menu_item')
        except:
            return 'There was an issue adding the menu item'
    else:
        menu_items = MenuItem.query.order_by(MenuItem.created_at).all()
        # first menu_index template is passed in, second is the var representing db query
        # menu_items contains all menu item queries, then used in template loop traversing the menu items
        return render_template('menu_index.html', menu_items=menu_items)
