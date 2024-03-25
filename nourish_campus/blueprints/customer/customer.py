from flask import Blueprint, render_template, request, redirect
from ...models.models import Customer
from ...extensions import db
from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField,
                     BooleanField)
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


customer_bp = Blueprint("customer", __name__, template_folder="templates")

@customer_bp.route("/customer", methods=['POST', 'GET'])
def greeting():
    return render_template('customer_index.html',
                           login_form=LoginForm(),
                           register_form=RegistrationForm())

# obsolete, delete later
def customer():
    if request.method == 'POST':
        name = request.form['name']
        daily_calories_goal = int(request.form['daily_calories_goal'])
        per_meal_calories_limit = int(request.form['per_meal_calories_limit'])
        new_customer = Customer(
            name=name, daily_calories_goal=daily_calories_goal, per_meal_calories_limit=per_meal_calories_limit)

        try:
            db.session.add(new_customer)
            db.session.commit()
            return redirect('/customer')
        except:
            return 'There was an issue adding the customer'
    else:
        customers = Customer.query.order_by(Customer.created_at).all()
        return render_template('customer_index.html', customers=customers)
