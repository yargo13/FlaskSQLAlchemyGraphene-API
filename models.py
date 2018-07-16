from sqlalchemy import *
from sqlalchemy.orm import relationship
from database import Base

class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    item = Column(String(50))
    person_id = Column(Integer, ForeignKey('person.id'), nullable = False)

    def __repr__(self):
        return self.item

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    chore = relationship('Todo', backref='person', lazy=True)
