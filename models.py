from sqlalchemy import *
from sqlalchemy.orm import relationship
from database import Base

class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    item = Column(String(50))
    def __repr__(self):
        return self.item
