from sqlalchemy import Column, Integer, String, Date, ForeignKey
from db.database import Base


class Booking(Base):
    __tablename__ = "Booking"

    id = Column(Integer, primary_key=True, index=True)
    passengerId = Column(Integer)
    couponId = Column(Integer, nullable=True)
    routeId = Column(Integer)
    bookingDate= Column(Date, nullable=False)
    bookingStatus = Column(String)
