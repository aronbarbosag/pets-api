from sqlalchemy import Column, String, Integer, ForeignKey
from src.models.sqlite.settings.base import Base


class People(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    pet_id = Column(Integer, ForeignKey("pets.id"))

    def __repr__(self):
        return f"People(first_name={self.first_name}, last_name={self.last_name}, age={self.age})"
