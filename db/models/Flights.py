from sqlalchemy import Column, Integer, String, Date, ForeignKey
from db.database import Base


class Flights(Base):
    __tablename__ = "Flights"

    id = Column(Integer, primary_key=True, index=True)
    aeroplaneName = Column(String, nullable=False, unique=True)
    airlinesName = Column(String, nullable=False)
    seatCapacity = Column(Integer, nullable=False)
    totalClass = Column(Integer, nullable=False)
    modelNo = Column(String, nullable=False)
    serialNo = Column(String, nullable=False, unique=True)
