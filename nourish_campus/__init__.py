from flask import Flask
from .extensions import db

from .blueprints.main.main import main_bp
from .blueprints.food_delivery.food_delivery import food_delivery_bp
from .blueprints.customer.customer import customer_bp
from .blueprints.menu_item.menu_item import menu_item_bp
from .blueprints.restaurant.restaurant import restaurant_bp
from .blueprints.order.order import order_bp
from .blueprints.order_item.order_item import order_item_bp

# from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)
    app.register_blueprint(food_delivery_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(menu_item_bp)
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(order_item_bp)

    return app


# try to remove the function create_app() later
app = create_app()

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# csrf = CSRFProtect(app) 
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    from .models.models import Customer
    return Customer.query.get(int(user_id))
