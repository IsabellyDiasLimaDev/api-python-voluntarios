from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session,sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///volunteers.bd',convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Volunteers(Base):
    __tablename__ = 'tblVolunteers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20),nullable=False)
    lastname = Column(String(20),nullable=False)
    neighborhood = Column(String(50),nullable=False)
    city = Column(String(30),nullable=False)

    def __repr__(self):
        return "<Voluntário: {}>".format(self.name)
    def save(self):
        db_session.add(self)
        db_session.commit()
    def delete(self):
        db_session.delete(self)
        db_session.commit()

class SocialActions(Base):
    __tablename__ = 'tblSocialActions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30),nullable=False)
    institution = Column(String(50),nullable=False)
    neighborhood = Column(String(50),nullable=False)
    city = Column(String(30),nullable=False)
    address = Column(String(100),nullable=False)
    description = Column(String(150),nullable=False)
    def __repr__(self):
        return "<Ação social: {}>".format(self.name)
    def save(self):
        db_session.add(self)
        db_session.commit()
    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
