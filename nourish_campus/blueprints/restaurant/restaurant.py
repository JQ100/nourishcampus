from flask import Blueprint, render_template, request, redirect
from ...models.models import Restaurant
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
        restaurants = Restaurant.query.order_by(Restaurant.id).all()
        return render_template('restaurant_index.html', restaurants=restaurants)
