from flask import Blueprint, render_template, request, redirect, url_for
from ...models.models import Customer
from ...extensions import db
from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, PasswordField, SubmitField,
                     BooleanField)
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange


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
    name = StringField('Name', validators=[DataRequired()])
    daily_calories_goal = IntegerField('Daily Calories Goal', validators=[DataRequired(), NumberRange(min=500, max=10000)])
    per_meal_calories_limit = IntegerField('Per Meal Calories Limit', validators=[
                                       DataRequired(), NumberRange(min=5, max=5000)])
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
    from ... import bcrypt
    if RegistrationForm().validate_on_submit():
        register_form = RegistrationForm()
        hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
        user = Customer(username=register_form.username.data,
                        email=register_form.email.data,
                        password=hashed_password, 
                        name=register_form.name.data, 
                        daily_calories_goal=register_form.daily_calories_goal.data,
                        per_meal_calories_limit=register_form.per_meal_calories_limit.data
                        )
        db.session.add(user)
        db.session.commit()
 
        user = Customer.query.filter_by(email =  
               RegistrationForm().email.data).first()
        if user and bcrypt.check_password_hash(user.password, RegistrationForm().password.data):
            login_user(user)
        return redirect(url_for('nourish_campus'))

    if LoginForm().validate_on_submit():
        login_form = LoginForm()
        user = Customer.query.filter_by(email =  
               login_form.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password, 
            login_form.password.data):
            
            login_user(user, remember = login_form.remember.data)
            
        return redirect(url_for('nourish_campus'))

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
