import os

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir, "voluntaries.db"))


SQLALCHEMY_DATABASE_URI = database_file