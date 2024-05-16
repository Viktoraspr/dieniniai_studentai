from sqlalchemy_project.constants import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_project.tables import Product, Customer, Order
from sqlalchemy_project.constants import URL


class DB:
    def __init__(self, url=URL):
        self.engine = create_engine(URL)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def __add_values_to_DB(self, obj: object):
        self.session.add(obj)
        self.session.commit()

    def add_products(self, **kwargs):
        product = kwargs.get('product')
        price = kwargs.get('price')
        ingredients = kwargs.get('ingredients')
        if not all([product, price, ingredients]):
            raise ValueError('We should get product, price and ingredients')
        extra = kwargs.get('extra')
        product = Product(
            product=product,
            price=price,
            ingredients=ingredients,
            extra=extra
        )
        self.__add_values_to_DB(product)
