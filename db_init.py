from nourish_campus.models.models import MenuItem, Customer, Restaurant, MealOrder, OrderItem

from sqlalchemy import create_engine
from nourish_campus.extensions import db
from nourish_campus import create_app, bcrypt
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
hashed_password = bcrypt.generate_password_hash("password").decode('utf-8')
customers = [
    Customer(email="jd101a@american.edu", password=hashed_password, name="John Doe", daily_calories_goal=2800, per_meal_calories_limit=1000)
]
db_session.add_all(customers)
db_session.commit()

# add restaurant
restaurants = [
    Restaurant(name="Starbucks", phone="202-885-7497", email="123@mail.com", address="Mary Graydon Center Tunnel"),
    Restaurant(name="Subway", phone="202-237-2424", email="123@mail.com", address="Mary Graydon Center Tunnel"),
    Restaurant(name="Qdoba", phone="901-846-3127", email="123@mail.com", address="Mary Graydon Center Tunnel"),
    Restaurant(name="Panera Bread", phone="202-885-3184", email="123@mail.com", address="Mary Graydon Center")

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
    MenuItem(name="6 inch Black Forest Ham Sub", price=5.89, calories=260, restaurant_id=2),
    MenuItem(name="6 inch All American Club Sub", price=7.69, calories=530, restaurant_id=2),
    MenuItem(name="6 inch Chicken & Bacon Ranch Melt Sub", price=6.59, calories=540, restaurant_id=2),
    MenuItem(name="6 inch Italian B.M.T Sub", price=6.49, calories=380, restaurant_id=2),
    MenuItem(name="6 inch Spicy Italian Sub", price=5.89, calories=450, restaurant_id=2),
    MenuItem(name="6 inch Steak & Cheese Sub", price=6.29, calories=340, restaurant_id=2),
    MenuItem(name="6 inch Tuna Sub", price=6.59, calories=450, restaurant_id=2),
    MenuItem(name="6 inch Meatball Marinara Sub", price=5.89, calories=430, restaurant_id=2),
    MenuItem(name="6 inch Veggie Delite Sub", price=5.29, calories=200, restaurant_id=2),
    MenuItem(name="6 inch Turkey Breast Sub", price=6.69, calories=250, restaurant_id=2),
    MenuItem(name="6 inch Roast Beef Sub", price=7.39, calories=290, restaurant_id=2),
    MenuItem(name="6 inch Rotisserie-Style Chicken Sub", price=6.19, calories=310, restaurant_id=2),
    MenuItem(name="6 inch B.L.T Sub", price=5.99, calories=340, restaurant_id=2),
    MenuItem(name="6 inch Buffalo Chicken Sub", price=6.89, calories=340, restaurant_id=2),
    MenuItem(name="6 inch Oven Roasted Turkey Sub", price=6.69, calories=260, restaurant_id=2),
    MenuItem(name="6 inch Teriyaki Chicken Sub", price=7.29, calories=353, restaurant_id=2),
    MenuItem(name="6 inch Subway Club Sub", price=6.99, calories=310, restaurant_id=2),
    MenuItem(name="6 inch Turkey B.L.T Sub", price=7.49, calories=340, restaurant_id=2),
    MenuItem(name="6 inch Cali Turkey Pro", price=8.89, calories=570, restaurant_id=2),
    MenuItem(name="6 inch The Monster", price=7.29, calories=540, restaurant_id=2),
    MenuItem(name="6 inch The Philly", price=6.69, calories=480, restaurant_id=2),
    MenuItem(name="6 inch The Outlaw", price=6.69, calories=440, restaurant_id=2),
    MenuItem(name="6 inch The Boss", price=7.59, calories=580, restaurant_id=2),
    MenuItem(name="6 inch The Mexicali", price=6.99, calories=540, restaurant_id=2),
    MenuItem(name="6 inch The Great Garlic", price=7.19, calories=570, restaurant_id=2),
    MenuItem(name="6 inch Titan Turkey", price=6.89, calories=490, restaurant_id=2),
    MenuItem(name="6 inch Garlic Roast Beef", price=7.79, calories=480, restaurant_id=2),
    MenuItem(name="6 inch The Beast", price=7.39, calories=730, restaurant_id=2),
    MenuItem(name="6 inch Grand Slam Ham", price=6.89, calories=416, restaurant_id=2),
    MenuItem(name="12 inch Black Forest Ham Sub", price=8.89, calories=520, restaurant_id=2),
    MenuItem(name="12 inch All American Club Sub", price=12.29, calories=890, restaurant_id=2),
    MenuItem(name="12 inch Sweet Onion Chicken Teriyaki Sub", price=11.39, calories=650, restaurant_id=2),
    MenuItem(name="12 inch Chicken & Bacon Ranch Melt Sub", price=12.79, calories=1070, restaurant_id=2),
    MenuItem(name="12 inch Veggie Delite Sub", price=7.69, calories=390, restaurant_id=2),
    MenuItem(name="12 inch Roast Beef Sub", price=10.39, calories=570, restaurant_id=2),
    MenuItem(name="12 inch Rotisserie-Style Chicken Sub", price=11.29, calories=630, restaurant_id=2),
    MenuItem(name="12 inch Buffalo Chicken Sub", price=10.59, calories=690, restaurant_id=2),
    MenuItem(name="12 inch Subway Melt Sub", price=10.19, calories=750, restaurant_id=2),
    MenuItem(name="12 inch Oven Roasted Turkey Sub", price=10.19, calories=530, restaurant_id=2),
    MenuItem(name="12 inch VegiMax Sub", price=8.39, calories=1040, restaurant_id=2),
    MenuItem(name="12 inch Subway Club Sub", price=10.29, calories=890, restaurant_id=2),
    MenuItem(name="12 inch The Monster", price=11.79, calories=1460, restaurant_id=2),
    MenuItem(name="12 inch The Philly", price=10.49, calories=1369, restaurant_id=2),
    MenuItem(name="12 inch The Outlaw", price=10.49, calories=1120, restaurant_id=2),
    MenuItem(name="12 inch The Boss", price=11.99, calories=1120, restaurant_id=2),
    MenuItem(name="12 inch The Great Garlic", price=12.59, calories=1290, restaurant_id=2),
    MenuItem(name="12 inch Titan Turkey", price=9.29, calories=980, restaurant_id=2),
    MenuItem(name="12 inch Garlic Roast Beef", price=11.09, calories=630, restaurant_id=2),
    MenuItem(name="12 inch The Beast", price=11.89, calories=1460, restaurant_id=2),
    MenuItem(name="12 inch Grand Slam Ham", price=9.29, calories=1000, restaurant_id=2),
    MenuItem(name="12 inch Tuna Bacon Guacamole", price=9.19, calories=1300, restaurant_id=2),
    MenuItem(name="12 inch Mexicali", price=12.39, calories=1140, restaurant_id=2),
    MenuItem(name="12 inch Supreme Meats", price=11.99, calories=900, restaurant_id=2),
    MenuItem(name="12 inch Turkey Breast Sub", price=10.19, calories=510, restaurant_id=2),
    MenuItem(name="Chipotle Southwest Steak & Cheese Wrap", price=9.69, calories=740, restaurant_id=2),
    MenuItem(name="B.L.T. Wrap", price=7.29, calories=600, restaurant_id=2),
    MenuItem(name="Black Forest Ham Wrap", price=8.89, calories=440, restaurant_id=2),
    MenuItem(name="Buffalo Chicken Wrap", price=10.59, calories=540, restaurant_id=2),
    MenuItem(name="Chicken Bacon Ranch Wrap", price=12.59, calories=800, restaurant_id=2),
    MenuItem(name="Cold Cut Combo Wrap", price=8.99, calories=560, restaurant_id=2),
    MenuItem(name="Meatball Marinara Wrap", price=8.99, calories=790, restaurant_id=2),
    MenuItem(name="Roast Beef Wrap", price=10.39, calories=490, restaurant_id=2),
    MenuItem(name="Rotisserie-Style Chicken Wrap", price=11.29, calories=680, restaurant_id=2),
    MenuItem(name="Steak & Cheese Wrap", price=9.69, calories=560, restaurant_id=2),
    MenuItem(name="Subway Club Wrap", price=10.99, calories=490, restaurant_id=2),
    MenuItem(name="Sweet Onion Chicken Teriyaki Wrap", price=11.39, calories=540, restaurant_id=2),
    MenuItem(name="Tuna Wrap", price=10.19, calories=820, restaurant_id=2),
    MenuItem(name="Turkey Breast Wrap", price=10.19, calories=430, restaurant_id=2),
    MenuItem(name="Veggie Delite Wrap", price=7.69, calories=330, restaurant_id=2),
    MenuItem(name="Black Forest Ham Chopped Salad", price=8.19, calories=120, restaurant_id=2),
    MenuItem(name="Oven Roasted Turkey Chopped Salad", price=8.99, calories=110, restaurant_id=2),
    MenuItem(name="Roast Beef Chopped Salad", price=9.69, calories=150, restaurant_id=2),
    MenuItem(name="Rotisserie-Style Chicken Chopped Salad", price=8.49, calories=170, restaurant_id=2),
    MenuItem(name="All American Club Chopped Salad", price=9.99, calories=230, restaurant_id=2),
    MenuItem(name="Sweet Onion Chicken Teriyaki Chopped Salad", price=9.59, calories=240, restaurant_id=2),
    MenuItem(name="Veggie Delite Chopped Salad", price=7.59, calories=60, restaurant_id=2),
    MenuItem(name="Chicken Bacon Ranch Chopped Salad", price=8.89, calories=460, restaurant_id=2),
    MenuItem(name="Cold Cut Combo Chopped Salad", price=8.19, calories=180, restaurant_id=2),
    MenuItem(name="Steak & Cheese Chopped Salad", price=8.59, calories=210, restaurant_id=2),
    MenuItem(name="Tuna Chopped Salad", price=8.89, calories=310, restaurant_id=2),
    MenuItem(name="Meatball Marinara Chopped Salad", price=8.19, calories=300, restaurant_id=2),
    MenuItem(name="Chips", price=1.39, calories=130, restaurant_id=2),
    MenuItem(name="Cookie", price=0.99, calories=200, restaurant_id=2),
    MenuItem(name="Vegetarian Burrito", price=9.85, calories=1070, restaurant_id=3),
    MenuItem(name="Grilled Adobo Chicken Burrito", price=10.45, calories=1175, restaurant_id=3),
    MenuItem(name="Cholula Hot Sweet Chicken Burrito", price=10.95, calories=900, restaurant_id=3),
    MenuItem(name="Ground Beef Burrito", price=10.45, calories=1250, restaurant_id=3),
    MenuItem(name="Grilled Steak Burrito", price=11.55, calories=1035, restaurant_id=3),
    MenuItem(name="Pulled Pork Burrito", price=10.95, calories=1055, restaurant_id=3),
    MenuItem(name="Brisket Birria Burrito", price=11.95, calories=1040, restaurant_id=3),
    MenuItem(name="Vegetarian Bowl", price=9.85, calories=555, restaurant_id=3),
    MenuItem(name="Grilled Adobo Chicken Bowl", price=10.45, calories=660, restaurant_id=3),
    MenuItem(name="Cholula Hot Sweet Chicken Bowl", price=10.95, calories=590, restaurant_id=3),
    MenuItem(name="Ground Beef Bowl", price=10.45, calories=770, restaurant_id=3),
    MenuItem(name="Grilled Steak Bowl", price=11.55, calories=650, restaurant_id=3),
    MenuItem(name="Pulled Pork Bowl", price=10.95, calories=525, restaurant_id=3),
    MenuItem(name="Brisket Birria Bowl", price=11.95, calories=490, restaurant_id=3),    
    MenuItem(name="3 Tacos - Vegetarian", price=9.85, calories=480, restaurant_id=3),
    MenuItem(name="3 Tacos - Grilled Adobo Chicken", price=10.45, calories=645, restaurant_id=3),
    MenuItem(name="3 Tacos - Cholula Hot Sweet Chicken", price=10.95, calories=510, restaurant_id=3),
    MenuItem(name="3 Tacos - Ground Beef", price=10.45, calories=585, restaurant_id=3),
    MenuItem(name="3 Tacos - Grilled Steak", price=11.55, calories=480, restaurant_id=3),
    MenuItem(name="3 Tacos - Pulled Pork", price=10.95, calories=420, restaurant_id=3),
    MenuItem(name="3 Tacos - Brisket Birria", price=11.95, calories=660, restaurant_id=3),
    MenuItem(name="Vegetarian Nachos", price=9.85, calories=1170, restaurant_id=3),
    MenuItem(name="Grilled Adobo Chicken Nachos", price=10.45, calories=1360, restaurant_id=3),
    MenuItem(name="Cholula Hot Sweet Chicken Nachos", price=10.95, calories=1220, restaurant_id=3),
    MenuItem(name="Ground Beef Nachos", price=10.45, calories=999, restaurant_id=3),
    MenuItem(name="Grilled Steak Nachos", price=11.55, calories=1010, restaurant_id=3),
    MenuItem(name="Pulled Pork Nachos", price=10.95, calories=1205, restaurant_id=3),
    MenuItem(name="Brisket Birria Nachos", price=11.95, calories=1520, restaurant_id=3),
    MenuItem(name="Vegetarian Taco Salad - No Shell", price=9.85, calories=490, restaurant_id=3),
    MenuItem(name="Vegetarian Taco Salad With Shell", price=9.85, calories=615, restaurant_id=3),
    MenuItem(name="Grilled Adobo Chicken Taco Salad - No Shell", price=10.45, calories=410, restaurant_id=3),
    MenuItem(name="Grilled Adobo Chicken Taco Salad With Shell", price=10.45, calories=500, restaurant_id=3),
    MenuItem(name="Cholula Hot Sweet Chicken Taco Salad - No Shell", price=10.95, calories=360, restaurant_id=3),
    MenuItem(name="Cholula Hot Sweet Chicken Taco Salad With Shell", price=10.95, calories=450, restaurant_id=3),
    MenuItem(name="Ground Beef Taco Salad - No Shell", price=10.45, calories=425, restaurant_id=3),
    MenuItem(name="Ground Beef Taco Salad With Shell", price=10.45, calories=525, restaurant_id=3),
    MenuItem(name="Grilled Steak Taco Salad - No Shell", price=11.55, calories=335, restaurant_id=3),
    MenuItem(name="Grilled Steak Taco Salad With Shell", price=11.55, calories=495, restaurant_id=3),
    MenuItem(name="Pulled Pork Taco Salad - No Shell", price=10.95, calories=340, restaurant_id=3),
    MenuItem(name="Pulled Pork Taco Salad With Shell", price=10.95, calories=460, restaurant_id=3),
    MenuItem(name="Brisket Birria Taco Salad - No Shell", price=11.95, calories=540, restaurant_id=3),
    MenuItem(name="Brisket Birria Taco Salad With Shell", price=11.95, calories=675, restaurant_id=3),
    MenuItem(name="Double Fudge Brownie", price=1.95, calories=360, restaurant_id=3),
    MenuItem(name="Chips and Salsa", price=3.95, calories=310, restaurant_id=3),
    MenuItem(name="Chips and Queso", price=6.25, calories=905, restaurant_id=3),
    MenuItem(name="Chips and Guacomole", price=5.25, calories=730, restaurant_id=3),
    MenuItem(name="Tuna & Tomato Soup Duet ", price=7.99, calories=600, restaurant_id=4),
    MenuItem(name="Grilled Cheese & Tomato Soup Duet", price=7.99, calories=680, restaurant_id=4),
    MenuItem(name="Smokehouse BBQ Chicken Sandwich & Tomato Soup Duet", price=7.99, calories=620, restaurant_id=4),
    MenuItem(name="Deli Ham Sandwich & Chicken Noodle Soup Duet", price=7.99, calories=360, restaurant_id=4),
    MenuItem(name="Autumn Squash Soup - Cup", price=7.19, calories=210, restaurant_id=4),
    MenuItem(name="Autumn Squash Soup - Bowl", price=8.69, calories=330, restaurant_id=4),
    MenuItem(name="Autumn Squash Soup - Bread Bowl", price=8.99, calories=880, restaurant_id=4),
    MenuItem(name="Creamy Tomato Soup - Cup", price=7.19, calories=240, restaurant_id=4),
    MenuItem(name="Creamy Tomato Soup - Bowl", price=8.69, calories=350, restaurant_id=4),
    MenuItem(name="Creamy Tomato Soup - Bread Bowl", price=8.99, calories=910, restaurant_id=4),
    MenuItem(name="Homestyle Chicken Noodle - Cup", price=7.19, calories=60, restaurant_id=4),
    MenuItem(name="Homestyle Chicken Noodle - Bowl", price=8.69, calories=100, restaurant_id=4),
    MenuItem(name="Homestyle Chicken Noodle - Bread Bowl", price=8.99, calories=730, restaurant_id=4),
    MenuItem(name="Broccoli Cheddar Soup - Cup", price=7.19, calories=240, restaurant_id=4),
    MenuItem(name="Broccoli Cheddar Soup - Bowl", price=8.69, calories=380, restaurant_id=4),
    MenuItem(name="Broccoli Cheddar Soup - Bread Bowl", price=8.99, calories=910, restaurant_id=4),
    MenuItem(name="Bistro French Onion Soup - Cup", price=7.19, calories=190, restaurant_id=4),
    MenuItem(name="Bistro French Onion Soup - Bowl", price=8.69, calories=310, restaurant_id=4),
    MenuItem(name="Bistro French Onion Soup - Bread Bowl", price=8.99, calories=860, restaurant_id=4),
    MenuItem(name="Cream of Chicken & Wild Rice Soup - Cup", price=7.19, calories=180, restaurant_id=4),
    MenuItem(name="Cream of Chicken & Wild Rice Soup - Bowl", price=8.69, calories=260, restaurant_id=4),
    MenuItem(name="Cream of Chicken & Wild Rice Soup - Bread Bowl", price=8.99, calories=840, restaurant_id=4),
    MenuItem(name="Turkey Chili Soup - Cup", price=7.59, calories=200, restaurant_id=4),
    MenuItem(name="Turkey Chili Soup - Bowl", price=9.79, calories=300, restaurant_id=4),
    MenuItem(name="Turkey Chili Soup - Bread Bowl", price=9.99, calories=870, restaurant_id=4),
    MenuItem(name="Mac & Cheese - Small", price=7.99, calories=480, restaurant_id=4),
    MenuItem(name="Mac & Cheese - Large", price=10.79, calories=960, restaurant_id=4),
    MenuItem(name="Mac & Cheese - Bread Bowl", price=10.19, calories=1150, restaurant_id=4),
    MenuItem(name="Half Greek Salad", price=6.99, calories=200, restaurant_id=4),
    MenuItem(name="Half Green Goddess Cobb Salad with Chicken", price=10.19, calories=250, restaurant_id=4),
    MenuItem(name="Half Caesar Salad", price=6.99, calories=170, restaurant_id=4),
    MenuItem(name="Half Caesar Salad with Chicken", price=8.99, calories=230, restaurant_id=4),
    MenuItem(name="Half Southwest Caesar Salad with Chicken", price=9.89, calories=320, restaurant_id=4),
    MenuItem(name="Whole Greek Salad", price=9.69, calories=400, restaurant_id=4),
    MenuItem(name="Whole Green Goddess Cobb Salad with Chicken", price=14.29, calories=500, restaurant_id=4),
    MenuItem(name="Whole Caesar Salad", price=9.69, calories=330, restaurant_id=4),
    MenuItem(name="Whole Caesar Salad with Chicken", price=12.39, calories=440, restaurant_id=4),
    MenuItem(name="Whole Southwest Caesar Salad with Chicken", price=13.79, calories=630, restaurant_id=4),
    MenuItem(name="Pepperoni Flatbread Pizza", price=11.79, calories=1070, restaurant_id=4),
    MenuItem(name="Margherita Flatbread Pizza", price=11.29, calories=870, restaurant_id=4),
    MenuItem(name="Cheese Flatbread Pizza", price=9.79, calories=920, restaurant_id=4),
    MenuItem(name="Mediterranean Bowl", price=11.29, calories=510, restaurant_id=4),
    MenuItem(name="Mediterranean Bowl with Chicken", price=13.49, calories=570, restaurant_id=4),
    MenuItem(name="Half Chipotle Chicken Avocado Melt Sandwich", price=8.89, calories=470, restaurant_id=4),
    MenuItem(name="Half Toasted Frontega Chicken Sandwich", price=8.89, calories=400, restaurant_id=4),
    MenuItem(name="Half Roasted Turkey & Avocado BLT Sandwich", price=9.89, calories=470, restaurant_id=4),
    MenuItem(name="Half Toasted Steak & White Cheddar Sandwich", price=9.89, calories=470, restaurant_id=4),
    MenuItem(name="Half Smokehouse BBQ Chicken Sandwich", price=7.89, calories=380, restaurant_id=4),
    MenuItem(name="Half Classic Grilled Cheese Sandwich", price=6.39, calories=440, restaurant_id=4),
    MenuItem(name="Half Tuna Salad Sandwich", price=6.29, calories=360, restaurant_id=4),
    MenuItem(name="Half Deli Turkey Sandwich", price=6.29, calories=300, restaurant_id=4),
    MenuItem(name="Half Deli Ham Sandwich", price=7.89, calories=290, restaurant_id=4),
    MenuItem(name="Half Mediterranean Veggie Sandwich", price=6.39, calories=320, restaurant_id=4),
    MenuItem(name="Half Grilled Mac & Cheese Sandwich", price=8.89, calories=440, restaurant_id=4),
    MenuItem(name="Pepperoni Mozzarella Melt", price=11.89, calories=1010, restaurant_id=4),
    MenuItem(name="Whole Chipotle Chicken Avocado Melt Sandwich", price=12.59, calories=940, restaurant_id=4),
    MenuItem(name="Whole Toasted Frontega Chicken Sandwich", price=12.59, calories=810, restaurant_id=4),
    MenuItem(name="Whole Roasted Turkey & Avocado BLT Sandwich", price=13.69, calories=940, restaurant_id=4),
    MenuItem(name="Whole Toasted Steak & White Cheddar Sandwich", price=13.69, calories=950, restaurant_id=4),
    MenuItem(name="Whole Bacon Turkey Bravo Sandwich", price=12.59, calories=1000, restaurant_id=4),
    MenuItem(name="Whole Classic Grilled Cheese Sandwich", price=8.69, calories=880, restaurant_id=4),
    MenuItem(name="Whole Smokehouse BBQ Chicken Sandwich", price=10.99, calories=760, restaurant_id=4),
    MenuItem(name="Whole Tuna Salad Sandwich", price=10.99, calories=720, restaurant_id=4),
    MenuItem(name="Whole Deli Turkey Sandwich", price=10.99, calories=590, restaurant_id=4),
    MenuItem(name="Whole Mediterranean Veggie Sandwich", price=8.69, calories=640, restaurant_id=4),
    MenuItem(name="Black Forest Ham & Gouda Melt", price=11.89, calories=960, restaurant_id=4),
    MenuItem(name="Green Goddess Caprese Melt", price=11.89, calories=970, restaurant_id=4),
    MenuItem(name="Pepperoni Chicken Melt", price=14.29, calories=1110, restaurant_id=4),
    MenuItem(name="Green Goddess Chicken Caprese Melt", price=14.29, calories=1070, restaurant_id=4),
    MenuItem(name="Cordon Bleu Melt", price=14.29, calories=1060, restaurant_id=4),
    MenuItem(name="Bacon Avocado Melt", price=10.39, calories=840, restaurant_id=4),
    MenuItem(name="Southwest Chicken Melt", price=10.39, calories=790, restaurant_id=4),
    MenuItem(name="Apple", price=1.29, calories=80, restaurant_id=4),
    MenuItem(name="Banana", price=1.29, calories=90, restaurant_id=4),
    MenuItem(name="French Baguette", price=0.99, calories=180, restaurant_id=4),
    MenuItem(name="Chips", price=1.29, calories=150, restaurant_id=4),
    MenuItem(name="Seasonal Fruit Cup", price=4.39, calories=60, restaurant_id=4),
    MenuItem(name="Hard Boiled Eggs - 2 Pack", price=2.49, calories=150, restaurant_id=4),
    MenuItem(name="Plain Cream Cheese Spread", price=1.70, calories=180, restaurant_id=4),
    MenuItem(name="Reduced Fat Chive & Onion Cream Cheese", price=1.70, calories=130, restaurant_id=4),
    MenuItem(name="Plain Bagel", price=1.89, calories=300, restaurant_id=4),
    MenuItem(name="Asiago Bagel", price=1.89, calories=300, restaurant_id=4),
    MenuItem(name="Blueberry Bagel", price=1.89, calories=300, restaurant_id=4),
    MenuItem(name="Multigrain Bagel", price=1.89, calories=180, restaurant_id=4),
    MenuItem(name="Cinnamon Crunch Bagel", price=1.89, calories=420, restaurant_id=4),
    MenuItem(name="Chocolate Chip Bagel", price=1.89, calories=330, restaurant_id=4),
    MenuItem(name="Plain Bagel", price=1.89, calories=300, restaurant_id=4),
    MenuItem(name="Cranberry Orange Muffin", price=3.99, calories=530, restaurant_id=4),
    MenuItem(name="Blueberry Muffin", price=3.99, calories=510, restaurant_id=4),
    MenuItem(name="Chocolate Chip Muffin", price=3.99, calories=340, restaurant_id=4),
    MenuItem(name="Brownie", price=3.79, calories=470, restaurant_id=4),
    MenuItem(name="Chocolate Chipper Cookie", price=2.99, calories=390, restaurant_id=4),
    MenuItem(name="Lemon Drop Cookie", price=2.99, calories=440, restaurant_id=4),
    MenuItem(name="Candy Cookie", price=2.99, calories=480, restaurant_id=4),
    MenuItem(name="Oatmeal Raisin with Berries Cookie", price=2.99, calories=350, restaurant_id=4),
    MenuItem(name="Kitchen Sink Cookie", price=4.99, calories=820, restaurant_id=4),
    MenuItem(name="Tulip Cookie", price=3.29, calories=440, restaurant_id=4),
    MenuItem(name="Blueberry Scone", price=3.99, calories=460, restaurant_id=4),
    MenuItem(name="Orange Scone", price=3.99, calories=550, restaurant_id=4),
    MenuItem(name="Chocolate Croissant", price=4.19, calories=410, restaurant_id=4),
    MenuItem(name="Hot Tea", price=2.99, calories=0, restaurant_id=4),
    MenuItem(name="Hot Coffee", price=2.59, calories=20, restaurant_id=4),
    MenuItem(name="Hot Chai Tea Latte - Regular", price=5.19, calories=290, restaurant_id=4),
    MenuItem(name="Hot Chai Tea Latte - Large", price=5.89, calories=370, restaurant_id=4),
    MenuItem(name="Hot Chocolate - Regular", price=4.49, calories=430, restaurant_id=4),
    MenuItem(name="Hot Chocolate - Large", price=4.89, calories=550, restaurant_id=4),
    MenuItem(name="Iced Cafe Blend Dark Roast Coffee - Regular", price=3.39, calories=15, restaurant_id=4),
    MenuItem(name="Iced Cafe Blend Dark Roast Coffee - Large", price=4.19, calories=25, restaurant_id=4),
    MenuItem(name="Madagascar Vanilla Cream Cold Brew - Regular", price=4.19, calories=190, restaurant_id=4),
    MenuItem(name="Madagascar Vanilla Cream Cold Brew - Large", price=4.49, calories=260, restaurant_id=4),
    MenuItem(name="Madagascar Vanilla Almond Cold Brew - Regular", price=4.19, calories=90, restaurant_id=4),
    MenuItem(name="Madagascar Vanilla Almond Cold Brew - Large", price=4.49, calories=120, restaurant_id=4),
    MenuItem(name="Cold Brew", price=3.79, calories=10, restaurant_id=4),
    MenuItem(name="Iced Chai Tea Latte", price=5.19, calories=290, restaurant_id=4),
    MenuItem(name="Mango Smoothie with Greek Yogurt", price=6.89, calories=300, restaurant_id=4),
    MenuItem(name="Strawberry Smoothie", price=6.89, calories=270, restaurant_id=4),
    MenuItem(name="Strawberry Banana Smoothie", price=6.89, calories=250, restaurant_id=4),
    MenuItem(name="Frozen Caramel Cold Brew", price=5.99, calories=490, restaurant_id=4),
    MenuItem(name="Frozen Chocolate Cold Brew", price=5.99, calories=450, restaurant_id=4),
    MenuItem(name="Bottled Water", price=2.59, calories=0, restaurant_id=4),
    MenuItem(name="Iced Tea", price=3.09, calories=10, restaurant_id=4),
    MenuItem(name="Orange Juice", price=3.49, calories=160, restaurant_id=4),
]
db_session.add_all(menuItems)
db_session.commit()