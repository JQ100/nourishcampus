from flask import Blueprint, render_template, request, redirect, url_for
from ...models.models import Customer
from ...extensions import db
from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, PasswordField, SubmitField,
                     BooleanField)
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange


class RegistrationForm(FlaskForm):
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
    # todo: add this to html
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


customer_bp = Blueprint("customer", __name__, template_folder="templates")

@customer_bp.route("/customer", methods=['POST', 'GET'])
def greeting():
    from ... import bcrypt
    if RegistrationForm().validate_on_submit():
        register_form = RegistrationForm()
        hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
        user = Customer(email=register_form.email.data,
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
        # return redirect(url_for('nourish_campus'))
        return redirect('/')

    if LoginForm().validate_on_submit():
        login_form = LoginForm()
        user = Customer.query.filter_by(email =  
               login_form.email.data).first()
        if not user:
            return render_template('views/user_not_found.html')
        
        if user and bcrypt.check_password_hash(user.password, 
            login_form.password.data):
            
            login_user(user, remember = login_form.remember.data)
            
        return redirect('/')

    if (request.method == "POST") & (request.form.get('post_header') == 'log out'):
        logout_user()
        return redirect('/')

    return render_template('customer_index.html',
                           login_form=LoginForm(),
                           register_form=RegistrationForm())
