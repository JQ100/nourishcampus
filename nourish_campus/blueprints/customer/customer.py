from flask import Blueprint, render_template, request, redirect
from ...models.models import Customer
from ...extensions import db

customer_bp = Blueprint("customer", __name__, template_folder="templates")

@customer_bp.route("/customer", methods=['POST', 'GET'])
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
