
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_project.constants import URL
from sqlalchemy_project.tables import Project


class DB:
    def __init__(self):
        self.engine = create_engine(URL)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_object_by_id(self, obj: object, id: int):
        return self.session.query(obj).get(id)

    def add_value_to_project_table(self, name, price):
        product = Project(name=name, price=price)
        self.session.add(product)
        self.session.commit()

    def add_values_to_project_table(self, data: list[tuple]):
        values = []
        for d in data:
            values.append(Project(name=d[0], price=d[1]))
        self.session.add_all(values)
        self.session.commit()
