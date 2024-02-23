from flask import Blueprint, render_template, request, redirect
from ...models.models import OrderItem
from ...extensions import db

order_item_bp = Blueprint("order_item", __name__, template_folder="templates")


@order_item_bp.route("/order_item", methods=['POST', 'GET'])
def order_item():
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
        order_items = OrderItem.query.order_by(OrderItem.created_at).all()
        return render_template('order_item_index.html', order_items=order_items)
