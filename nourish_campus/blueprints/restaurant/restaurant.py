from flask import Blueprint, render_template, request, redirect
from ...models.models import Restaurant, MenuItem
from ...extensions import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_login import current_user


class RestaurantUpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Update Restaurant')


restaurant_bp = Blueprint(
    "restaurant",
    __name__,
    template_folder="templates",
    static_folder='static',
)


@restaurant_bp.route("/restaurant", methods=["GET", "POST"])
def handle_restaurant():
    if request.method == 'POST':
        if not current_user.is_admin:
            return "You are not authorized to add a restaurant."
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']

        restaurant = Restaurant(
            name=name, phone=phone, email=email, address=address)

        try:
            db.session.add(restaurant)
            db.session.commit()
            return redirect('/restaurant')
        except:
            return 'There was an issue adding the restaurant'
    else:
        return render_all_undeleted_restaurants()


# example url: http://localhost:5000/restaurant/update/3
@restaurant_bp.route("/restaurant/update/<int:restaurant_id>", methods=["GET", "POST"])
def update_restaurant(restaurant_id):
    if request.method == "POST":
        if not current_user.is_admin:
            return "You are not authorized to update a restaurant."

        updateForm = RestaurantUpdateForm()
        if updateForm.validate():
            restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
            restaurant.name = updateForm.name.data
            restaurant.address = updateForm.address.data
            restaurant.phone = updateForm.phone.data
            restaurant.email = updateForm.email.data

            db.session.commit()
            return redirect('/restaurant')
        else:
            # print the form errors for debugging
            print(updateForm.errors)
            return "There are errors in your update restaurant form."
    else:
        # GET
        restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
        updateForm = RestaurantUpdateForm()
        # pre-fill the data with the restaurant info
        updateForm.email.data = restaurant.email
        updateForm.address.data = restaurant.address
        updateForm.phone.data = restaurant.phone
        updateForm.name.data = restaurant.name
        return render_template('restaurant_update.html', update_form=updateForm)


@restaurant_bp.route("/restaurant/delete", methods=["POST"])
def del_restaurant():
    if not current_user.is_admin:
        return "You are not authorized to delete a restaurant."

    restaurant_id = request.form['restaurant_id']

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

