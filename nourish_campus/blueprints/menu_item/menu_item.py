from flask import Blueprint, render_template, request, redirect
from ...models.models import MenuItem, Restaurant
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from ...extensions import db
from flask_login import current_user

menu_item_bp = Blueprint("menu_item", __name__, template_folder="templates")

class MenuUpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    calories = StringField('Calories', validators=[DataRequired()])
    submit = SubmitField('Update Menu Item')


@menu_item_bp.route("/menu_item", methods=['POST'])
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
        restaurant_id=restaurant_id, is_soft_deleted=False).order_by(MenuItem.created_at).all()
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first()

    # first menu_index template is passed in, second is the var representing db query
    # menu_items contains all menu item queries, then used in template loop traversing the menu items
    return render_template('menu_index.html', menu_items=menu_items, restaurant=restaurant)

@menu_item_bp.route("/menu_item/update/<int:restaurant_id>/<int:menu_item_id>", methods=["GET", "POST"])
def update_menu_item(restaurant_id, menu_item_id):
    if request.method == "POST":
        # POST
        updateForm = MenuUpdateForm()
        if updateForm.validate():
            menu_item = MenuItem.query.filter_by(id=menu_item_id).first()
            menu_item.name = updateForm.name.data
            menu_item.price = updateForm.price.data
            menu_item.calories = updateForm.calories.data

            db.session.commit()
            return redirect('/menu_item/{restaurant_id}')
        else:
            # print the form errors for debugging
            print(updateForm.errors)
            return "There are errors in your update menu item form."
    else:
        # GET
        menu_item = MenuItem.query.filter_by(id=menu_item_id).first()
        updateForm = MenuUpdateForm()
        # pre-fill the data with the menu item info
        updateForm.name.data = menu_item.name
        updateForm.price.data = menu_item.price
        updateForm.calories.data = menu_item.calories
        return render_template('menu_update.html', update_form=updateForm)


@menu_item_bp.route("/menu_item/delete/<int:restaurant_id>/<int:menu_item_id>")
def del_menu_item(restaurant_id, menu_item_id):
    menu_item = MenuItem.query.filter_by(id=menu_item_id).first()
    menu_item.is_soft_deleted = True
    db.session.commit()

    return redirect(f'/menu_item/{restaurant_id}')
