from sqlalchemy_project.constants import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_project.tables import Product, Customer, Order
from sqlalchemy_project.db_management import DB


db = DB()
# db.add_products(
#     product='Avienos',
#     price=10.00,
#     ingredients='lamb, vegetables, baton, onions',
#     extra='peppers'
# )

db.add_products(
    product='Avienos',
    extra='peppers'
)



#
# engine = create_engine(URL)
# Session = sessionmaker(bind=engine)
# session = Session()

# product = Product(
#     product='Arnoldo kebabas didesnis',
#     price=3.50,
#     ingredients='beef, vegetables, baton, onions',
#     extra='peppers'
# )
#
# customer = Customer(
#     name='Giedrius',
#     phone_number='860059408'
# )
#
# session.add_all([product, customer])

# customer = session.query(Customer).get(1)
# product = session.query(Product).get(2)
#
# order = Order(
#     customer_id=customer.customer_id,
#     product_id=product.product_id,
#     quantity=2
# )

# session.add(order)
#
# values = session.query(Order).all()
#
# print(values)
#
# order: Order
# order = session.query(Order).get(2)
# order.quantity = 5

# order: Order
# order = session.query(Order).get(2)
# session.delete(order)
#
# session.commit()
