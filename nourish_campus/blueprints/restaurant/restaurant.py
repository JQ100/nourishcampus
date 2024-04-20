from flask import Blueprint, render_template, request, redirect
from ...models.models import Restaurant, MenuItem
from ...extensions import db

restaurant_bp = Blueprint(
    "restaurant",
    __name__,
    template_folder="templates",
    static_folder='static',
)


@restaurant_bp.route("/restaurant", methods=["GET", "POST"])
def restaurant():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']

        new_menu_item = Restaurant(
            name=name, phone=phone, email=email, address=address)

        try:
            db.session.add(new_menu_item)
            db.session.commit()
            return redirect('/restaurant')
        except:
            return 'There was an issue adding the restaurant'
    else:
        return render_all_undeleted_restaurants()


@restaurant_bp.route("/restaurant/delete/<int:restaurant_id>")
def del_restaurant(restaurant_id):
    # delete from restaurant where id=restaurant_id
    # do this: is_soft_deleted = True
    #   update restaurant set is_soft_deleted = True where id=restaurant_id
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
    restaurant.is_soft_deleted = True

    # also delete the menu items for the restaurant
    # select * from MenuItem where restaurant_id = restaurant_id
    # update ...
    items = MenuItem.query.filter_by(restaurant_id=restaurant_id).all()
    for item in items:
        item.is_soft_deleted = True

    db.session.commit()
    return redirect(f'/restaurant')

def render_all_undeleted_restaurants():
    restaurants = Restaurant.query.order_by(
        Restaurant.id).filter_by(is_soft_deleted=False).all()
    return render_template('restaurant_index.html', restaurants=restaurants)

