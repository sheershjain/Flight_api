from sqlalchemy import Column, Integer, String, ForeignKey
from db.database import Base


class Routes(Base):
    __tablename__ = "Routes"

    id = Column(Integer, primary_key=True, index=True)
    sourceCityName = Column(String)
    destinationCityName = Column(String)
    flightId = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    startingTime = Column(String, nullable=False)
    endingTime = Column(String, nullable=False)
