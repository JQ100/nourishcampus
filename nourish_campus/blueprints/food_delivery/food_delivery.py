from flask import Blueprint, render_template, request, redirect
from ...models.models import Customer, MealOrder, OrderItem, MenuItem
from ...extensions import db
from datetime import datetime

food_delivery_bp = Blueprint("food_delivery", __name__, template_folder="templates")


@food_delivery_bp.route("/food_delivery")
def food_delivery():
    customers = Customer.query.all()
    return render_template('food_delivery_index.html', customers=customers)

@food_delivery_bp.route("/food_delivery/customer/<int:id>")
def customer(id):
    # find the customer
    customers = Customer.query.filter_by(id=id).all()
    if not customers:
        return f'customer {id} not found'
    
    customer = customers[0]
    menuItemsByOrderId = getOrderedMealsByCustomerOnDate(
        customer.id, datetime.now().date())
    
    totalCalories = getCalories(menuItemsByOrderId)

    suggestedMeal = suggestAMeal(totalCalories, customer)
    suggestedMealQueryString = '&'.join(f'item={item.id}' for item in suggestedMeal)
    return render_template('customer.html', 
                           customer=customers[0], 
                           totalCalories=totalCalories,
                           menuItemsByOrderId=menuItemsByOrderId,
                           suggestedMeal=suggestedMeal,
                           suggestedMealQueryString=suggestedMealQueryString)

def suggestAMeal(totalConsumedCalories: int, customer: Customer) -> list[MenuItem]:
    import random
    items = MenuItem.query.all()

    availableCalories = min(customer.daily_calories_goal - totalConsumedCalories, customer.per_meal_calories_limit)
    meal = []
    while items and availableCalories > 0:
        item = random.choice(items)
        items.remove(item)
        if item.calories <= availableCalories:
            meal.append(item)
            availableCalories -= item.calories
    return meal

def getCalories(menuItemsByOrderId):
    totalCalories = 0
    for _, menuItems in menuItemsByOrderId.items():
        totalCalories += sum(menuItem.calories for menuItem in menuItems) if menuItems else 0
    return totalCalories

def getOrderedMealsByCustomerOnDate(customerId, date):
    # get the customer's previous orders of the same date
    orders = MealOrder.query.filter_by(
        customer_id=customerId, created_at=date).all()

    # get all the menu items in the orders
    # {orderId: [menuItems]}
    menuItemsByOrderId = {}
    for order in orders:
        orderItems = OrderItem.query.filter_by(
            order_id=order.id).all()
        menuItems = []
        for orderItem in orderItems:
            menuItem = MenuItem.query.filter_by(id=orderItem.menu_item_id).all()
            menuItems.extend(menuItem)
        menuItemsByOrderId[order.id] = menuItems
    return menuItemsByOrderId

@food_delivery_bp.route("/food_delivery/order/")
def order():
    customerId = request.args.get("customer")
    itemIds = request.args.getlist("item")

    if not itemIds:
        return redirect(f'/food_delivery/customer/{customerId}')

    name = "meal" # todo: let user specify the meal name
    payment = 20 # todo: may pass the payment in customer.html
    new_order = MealOrder(name=name, customer_id=customerId, payment=payment)
    try:
        db.session.add(new_order)
        db.session.commit()
    except:
        return 'There was an issue adding your order'
    
    for item_id in itemIds:
        new_order_item = OrderItem(order_id=new_order.id, menu_item_id=item_id)
        try:
            db.session.add(new_order_item)
            db.session.commit()
        except:
            return 'There was an issue adding your order details'

    return redirect(f'/food_delivery/customer/{customerId}')
