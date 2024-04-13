from flask import Blueprint, render_template, request, redirect
from ...models.models import OrderItem, MealOrder
from ...extensions import db
from flask_login import current_user

order_item_bp = Blueprint("order_item", __name__, template_folder="templates")


@order_item_bp.route("/order_item", methods=['POST', 'GET'])
def order_item():
    if not current_user.is_authenticated:
        return redirect('/customer')
    
    if request.method == 'POST':
        # todo
        name = request.form['name']
        new_order_item = OrderItem(name=name)

        try:
            db.session.add(new_order_item)
            db.session.commit()
            return redirect('/order_item')
        except:
            return 'There was an issue adding your task'

    else:
        # gets all the orders from the current user
        orders = MealOrder.query.filter_by(
            customer_id=current_user.id).order_by(MealOrder.created_at).all()

        # get all the ordered items from the order ids of the orders of the current user.
        order_ids = [order.id for order in orders]
        all_order_items_for_user = []
        for order_id in order_ids:
            order_items = OrderItem.query.filter_by(
                order_id=order_id).order_by(OrderItem.created_at).all()
            all_order_items_for_user.extend(order_items)
    
        return render_template('order_item_index.html', order_items=all_order_items_for_user)

@order_item_bp.route("/order_item/<int:order_id>", methods=['GET'])
def get_order_items(order_id):
    order_items = OrderItem.query.filter_by(
        order_id=order_id).order_by(OrderItem.created_at).all()

    return render_template('order_item_index.html', order_items=order_items)