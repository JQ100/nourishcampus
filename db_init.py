from nourish_campus.models.models import MenuItem, Customer, Restaurant, MealOrder, OrderItem

from sqlalchemy import create_engine
from nourish_campus import db
from nourish_campus.extensions import db
from nourish_campus import create_app
from nourish_campus.models import *

from sqlalchemy.orm import Session

# create all the tables in models directory
db.create_all(app=create_app())

# initialize a db session
engine = create_engine('sqlite:///nourish_campus/db.sqlite3', echo=True)
db_session = Session(engine)

# Delete old data in the tables
db_session.query(Customer).delete()
db_session.query(Restaurant).delete()
db_session.query(MenuItem).delete()
db_session.query(MealOrder).delete()
db_session.query(OrderItem).delete()
db_session.commit()

# add customers
customers = [
    Customer(name="John Doe", daily_calories_goal=2800, per_meal_calories_limit=1000)
]
db_session.add_all(customers)
db_session.commit()

# add restaurant
restaurants = [
    Restaurant(name="Starbucks", phone="202-885-7497", email="123@mail.com", address="Mary Graydon Center Tunnel")
]
db_session.add_all(restaurants)
db_session.commit()
# add menu items
menuItems = [
    MenuItem(name="Caffe Mocha", price=8.45, calories=370, restaurant_id=1),
    MenuItem(name="Cappuccino", price=7.95, calories=140, restaurant_id=1),
    MenuItem(name="Caffe Misto", price=4.45, calories=110, restaurant_id=1),
    MenuItem(name="Espresso Macchiato", price=7.55, calories=15, restaurant_id=1),
    MenuItem(name="Espresso", price=5.45, calories=10, restaurant_id=1),
    MenuItem(name="Honey Almondmilk Flat White", price=7.45, calories=170, restaurant_id=1),
    MenuItem(name="Caramel Macchiato", price=9.95, calories=250, restaurant_id=1),
    MenuItem(name="Caffe Americano", price=7.45, calories=15, restaurant_id=1),
    MenuItem(name="Honey Oatmilk Latte", price=8.45, calories=250, restaurant_id=1),
    MenuItem(name="Flat White", price=8.45, calories=220, restaurant_id=1),
    MenuItem(name="Espresso con Panna", price=5.85, calories=35, restaurant_id=1),
    MenuItem(name="Steamed Milk", price=4.65, calories=200, restaurant_id=1),
    MenuItem(name="Peppermint Hot Chocolate", price=4.75, calories=440, restaurant_id=1),
    MenuItem(name="Peppermint White Hot Chocolate", price=4.75, calories=520, restaurant_id=1),
    MenuItem(name="Blonde Vanilla Latte", price=8.65, calories=250, restaurant_id=1),
    MenuItem(name="Coffee", price=3.65, calories=5, restaurant_id=1),
    MenuItem(name="Iced Flat White", price=7.65, calories=150, restaurant_id=1),
    MenuItem(name="Iced Caramel Macchiato", price=9.95, calories=250, restaurant_id=1),
    MenuItem(name="Iced Honey Oatmilk Latte", price=7.25, calories=230, restaurant_id=1),
    MenuItem(name="Vanilla Sweet Cream Cold Brew", price=6.25, calories=110, restaurant_id=1),
    MenuItem(name="Cold Brew Coffee", price=4.95, calories=5, restaurant_id=1),
    MenuItem(name="Salted Caramel Cream Cold Brew", price=5.75, calories=240, restaurant_id=1),
    MenuItem(name="Honey Almondmilk Cold Brew", price=5.45, calories=55, restaurant_id=1),
    MenuItem(name="Iced Coffee", price=4.75, calories=80, restaurant_id=1),
    MenuItem(name="Iced White Chocolate Mocha", price=8.25, calories=390, restaurant_id=1),
    MenuItem(name="Iced Caffe Americano", price=7.15, calories=15, restaurant_id=1),
    MenuItem(name="Iced Cinnamon Dolce Latte", price=7.55, calories=300, restaurant_id=1),
    MenuItem(name="Iced Blonde Vanilla Latte", price=8.05, calories=190, restaurant_id=1),
    MenuItem(name="Iced Espresso con Panna", price=5.85, calories=35, restaurant_id=1),
    MenuItem(name="Iced Espresso", price=5.75, calories=10, restaurant_id=1),
    MenuItem(name="Chocolate Creme Cold Brew", price=5.45, calories=250, restaurant_id=1),
    MenuItem(name="Iced Caffe Latte", price=7.25, calories=130, restaurant_id=1),
    MenuItem(name="Iced Caffe Mocha", price=7.75, calories=350, restaurant_id=1),
    MenuItem(name="Iced Peppermint White Chocolate Mocha", price=4.75, calories=490, restaurant_id=1),
    MenuItem(name="Caramel Apple Spice", price=6.25, calories=380, restaurant_id=1),
    MenuItem(name="Hot Chocolate", price=6.65, calories=370, restaurant_id=1),
    MenuItem(name="White Hot Chocolate", price=7.05, calories=400, restaurant_id=1),
    MenuItem(name="Cinnamon Dolce Latte", price=6.55, calories=340, restaurant_id=1),
    MenuItem(name="Vanilla Creme", price=4.75, calories=350, restaurant_id=1),
    MenuItem(name="London Fog Tea Latte", price=8.05, calories=180, restaurant_id=1),
    MenuItem(name="Honey Citrus Mint Tea", price=4.75, calories=130, restaurant_id=1),
    MenuItem(name="Chai Tea Latte", price=6.25, calories=240, restaurant_id=1),
    MenuItem(name="Emperor's Clouds & Mist Tea", price=2.65, calories=0, restaurant_id=1),
    MenuItem(name="Matcha Green Tea Latte", price=11.75, calories=240, restaurant_id=1),
    MenuItem(name="Citrus Defender", price=3.75, calories=130, restaurant_id=1),
    MenuItem(name="Pink Drink", price=5.75, calories=140, restaurant_id=1),
    MenuItem(name="Dragon Drink", price=7.45, calories=130, restaurant_id=1),
    MenuItem(name="Mango Dragonfruit Refresher", price=6.25, calories=90, restaurant_id=1),
    MenuItem(name="Mango Dragonfruit Lemonade Refresher", price=7.75, calories=140, restaurant_id=1),
    MenuItem(name="Strawberry Acai Refresher", price=6.05, calories=100, restaurant_id=1),
    MenuItem(name="Strawberry Acai Lemonade Refresher", price=6.75, calories=140, restaurant_id=1),
    MenuItem(name="Pineapple Passionfruit Refresher", price=5.25, calories=100, restaurant_id=1),
    MenuItem(name="Pineapple Passionfruit Lemonade Refresher", price=5.75, calories=140, restaurant_id=1),
    MenuItem(name="Paradise Drink", price=5.75, calories=140, restaurant_id=1),
    MenuItem(name="Frozen Strawberry Acai Lemonade Refresher", price=7.85, calories=160, restaurant_id=1),
    MenuItem(name="Frozen Mango Dragonfruit Lemonade Refresher", price=7.85, calories=150, restaurant_id=1),
    MenuItem(name="Cinnamon Caramel Cream Cold Brew", price=6.50, calories=250, restaurant_id=1),
    MenuItem(name="Cinnamon Caramel Cream Nitro", price=7.00, calories=260, restaurant_id=1),
    MenuItem(name="Iced Matcha Green Tea Latte", price=9.25, calories=200, restaurant_id=1),
    MenuItem(name="Iced Chai Tea Latte", price=5.55, calories=240, restaurant_id=1),
    MenuItem(name="Iced Matcha Lemonade", price=5.75, calories=120, restaurant_id=1),
    MenuItem(name="Iced Black Tea Lemonade", price=4.95, calories=50, restaurant_id=1),
    MenuItem(name="Iced Green Tea Lemonade", price=4.95, calories=50, restaurant_id=1),
    MenuItem(name="Iced Peach Green Tea", price=4.95, calories=60, restaurant_id=1),
    MenuItem(name="Iced Passion Tango Tea", price=3.45, calories=0, restaurant_id=1),
    MenuItem(name="Iced Black Tea", price=3.25, calories=0, restaurant_id=1),
    MenuItem(name="Iced Green Tea", price=3.25, calories=0, restaurant_id=1),
    MenuItem(name="Iced Peach Green Tea Lemonade", price=4.75, calories=80, restaurant_id=1),
    MenuItem(name="Iced Peach Green Tea", price=4.75, calories=60, restaurant_id=1),
    MenuItem(name="Iced Black Tea Lemonade", price=4.25, calories=50, restaurant_id=1),
    MenuItem(name="Caramel Ribbon Crunch Frappuccino", price=6.75, calories=470, restaurant_id=1),
    MenuItem(name="Mocha Cookie Crumble Frappuccino", price=6.75, calories=480, restaurant_id=1),
    MenuItem(name="Strawberry Frappuccino", price=6.45, calories=370, restaurant_id=1),
    MenuItem(name="Caramel Frappuccino", price=6.45, calories=380, restaurant_id=1),
    MenuItem(name="Mocha Frappuccino", price=6.45, calories=370, restaurant_id=1),
    MenuItem(name="Coffee Frappuccino", price=6.15, calories=230, restaurant_id=1),
    MenuItem(name="Java Chip Frappuccino", price=6.45, calories=440, restaurant_id=1),
    MenuItem(name="Vanilla Bean Creme Frappuccino", price=6.15, calories=380, restaurant_id=1),
    MenuItem(name="Double Chocolaty Creme Frappuccino", price=6.45, calories=410, restaurant_id=1),
    MenuItem(name="Matcha Creme Frappuccino", price=6.45, calories=420, restaurant_id=1),
    MenuItem(name="Espresso Frappuccino", price=6.75, calories=210, restaurant_id=1),
    MenuItem(name="Peppermint Mocha Frappuccino", price=5.45, calories=430, restaurant_id=1),
    MenuItem(name="Strawberry Creme Frappuccino", price=6.25, calories=370, restaurant_id=1),
    MenuItem(name="Blueberry Scone", price=3.65, calories=380, restaurant_id=1),
    MenuItem(name="Classic Coffee Cake", price=3.95, calories=330, restaurant_id=1),
    MenuItem(name="Petite Vanilla Bean Scone", price=2.45, calories=120, restaurant_id=1),
    MenuItem(name="Old Fashioned Glazed Doughnut", price=2.95, calories=480, restaurant_id=1),
    MenuItem(name="Blueberry Muffin", price=3.95, calories=360, restaurant_id=1),
    MenuItem(name="Banana Nut Bread", price=4.65, calories=420, restaurant_id=1),
    MenuItem(name="Iced Lemon Loaf Cake", price=4.65, calories=470, restaurant_id=1),
    MenuItem(name="Pumpkin Bread", price=4.65, calories=410, restaurant_id=1),
    MenuItem(name="Butter Croissant", price=4.26, calories=260, restaurant_id=1),
    MenuItem(name="Chocolate Croissant", price=4.45, calories=340, restaurant_id=1),
    MenuItem(name="Cheese Danish", price=3.95, calories=290, restaurant_id=1),
    MenuItem(name="Plain Bagel", price=2.95, calories=280, restaurant_id=1),
    MenuItem(name="Everything Bagel", price=2.95, calories=290, restaurant_id=1),
    MenuItem(name="Avocado Spread", price=1.45, calories=90, restaurant_id=1),
    MenuItem(name="Chocolate Cake Pop", price=3.75, calories=160, restaurant_id=1),
    MenuItem(name="Chocolate Chip Cookie", price=3.25, calories=360, restaurant_id=1),
    MenuItem(name="Double Chocolate Chunk Brownie", price=3.95, calories=480, restaurant_id=1),
    MenuItem(name="Ham & Cheese Croissant", price=4.65, calories=320, restaurant_id=1),
    MenuItem(name="Marshmallow Dream Bar", price=2.50, calories=230, restaurant_id=1),
    MenuItem(name="Birthday Cake Pop", price=3.75, calories=170, restaurant_id=1),
    MenuItem(name="Classic Oatmeal", price=5.50, calories=160, restaurant_id=1),
    MenuItem(name="Cookies and Cream Cake Pop", price=3.75, calories=160, restaurant_id=1),
    MenuItem(name="Valentine Cake Pop", price=3.95, calories=140, restaurant_id=1),
    MenuItem(name="Vanilla Bean Custard Danish", price=4.25, calories=230, restaurant_id=1),
    MenuItem(name="Chicken, Maple Butter & Egg Sandwich", price=6.45, calories=420, restaurant_id=1),
    MenuItem(name="Bacon, Sausage & Egg Wrap", price=7.25, calories=640, restaurant_id=1),
    MenuItem(name="Spinach, Feta & Egg White Wrap", price=5.65, calories=290, restaurant_id=1),
    MenuItem(name="Double-Smoked Bacon, Cheddar & Egg Sandwich", price=6.45, calories=500, restaurant_id=1),
    MenuItem(name="Turkey, Bacon & Egg-White Sandwich", price=5.45, calories=230, restaurant_id=1),
    MenuItem(name="Bacon & Gruyere Egg Bites", price=5.65, calories=300, restaurant_id=1),
    MenuItem(name="Egg White & Roasted Red Pepper Egg Bites", price=5.65, calories=170, restaurant_id=1),
    MenuItem(name="Kale and Mushroom Egg Bites", price=5.65, calories=230, restaurant_id=1),
    MenuItem(name="Oleato Caffe Latte with Oatmilk", price=6.75, calories=330, restaurant_id=1),
    MenuItem(name="Iced Chai Tea Latte with Oleato Golden Foam", price=10.85, calories=510, restaurant_id=1),
    MenuItem(name="Oleato Iced Shaken Espresso with Oatmilk and Toffeenut", price=8.45, calories=360, restaurant_id=1),
    MenuItem(name="Dragon Drink Refresher with Oleato Golden Foam", price=8.95, calories=380, restaurant_id=1),
    MenuItem(name="Paradise Drink Refresher with Oleato Golden Foam", price=8.95, calories=390, restaurant_id=1),
    MenuItem(name="Iced Matcha Tea Latte with Oleato Golden Foam", price=9.25, calories=410, restaurant_id=1),

]
db_session.add_all(menuItems)
db_session.commit()