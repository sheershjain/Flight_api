from sqlalchemy import Column, Integer, String, ForeignKey
from db.database import Base


class Passenger(Base):
    __tablename__ = "Passenger"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    contactNo = Column(String, nullable=False, unique=True)
    address = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
