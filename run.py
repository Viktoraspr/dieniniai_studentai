from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_project.constants import URL
from sqlalchemy_project.db_management import DB
from sqlalchemy_project.tables import Project


# engine = create_engine(URL)
# Session = sessionmaker(bind=engine)
# session = Session()

db = DB()
# db.add_value_to_project_table(name='Suknele', price=99.99)

products = [
    ('Švarkas', 119.99),
    ('Šortai', 39.99),
    ('Marškiniai', 49.99),
]

db.add_values_to_project_table(products)

# value = db.get_object_by_id(Project, 2)
#
# print(value.name)
#

# project = Project(
#     name="Hat",
#     price=39.99,
# )
# session.add(project)
# session.commit()
# project_1 = Project(
#     name="Pans",
#     price=59.99,
# )
#
# projects = [project, project_1]
# session.add_all(projects)
# session.commit()

# projektas1 = session.query(Project).get(1)

# projektas2 = session.query(Project).filter_by(name='Hat').all()
# print(projektas2)

#
# search = session.query(Project).filter(Project.name.ilike("H%")).all()
# print(search)

# hat = session.query(Project).get(1)
# hat.name = 'Dresses'
# session.commit()

# session.delete(hat)
# session.commit()
