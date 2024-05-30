from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Task(Base):
    __tablename__="tasks"
    id = Column(Integer, primary_key=True)
    project = relationship("Project", back_populates="tasks")