from enum import unique
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base


class Flights(Base):
    __tablename__ = "Flights"

    id = Column(Integer, primary_key=True, index=True)
    aeroplaneName = Column(String, nullable=False, unique=True)
    airlinesName = Column(String, nullable=False)
    seatCapacity = Column(Integer, nullable=False, unique=True)
    availableSeats = Column(Integer, nullable=False)
    totalClass = Column(Integer, nullable=False)
    modelNo = Column(String, nullable=False, unique=True)
    serialNo = Column(String, nullable=False, unique=True)


class Routes(Base):
    __tablename__ = "Routes"

    id = Column(Integer, primary_key=True, index=True)
    sourceCityName = Column(String)
    destinationCityName = Column(String)
    flightId = Column(Integer, ForeignKey("Flights.id"), unique=True, nullable=False)
    amount = Column(Integer, nullable=False)
    startingTime = Column(String, nullable=False)
    endingTime = Column(String, nullable=False)


class Passenger(Base):
    __tablename__ = "Passenger"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    contactNo = Column(String, nullable=False)
    address = Column(String, nullable=False)
    age = Column(Integer, nullable=False)


class Coupon(Base):
    __tablename__ = "Discount"

    id = Column(Integer, primary_key=True, index=True)
    couponNo = Column(String, nullable=False)
    couponValue = Column(String, nullable=False)
    issueDate = Column(Date, nullable=False)
    amount = Column(Integer, nullable=False)


class Payment(Base):
    __tablename__ = "Transaction"

    id = Column(Integer, primary_key=True, index=True)
    bankName = Column(String, nullable=False)
    paymentMode = Column(String, nullable=False)
    bookingId = Column(Integer, ForeignKey("Booking.id"), nullable=False)
    date = Column(Date, nullable=False)
    amount = Column(Integer, nullable=False)
    couponStatus = Column(String)
    finalAmount = Column(Integer)
    paymentStatus = Column(String)


class Booking(Base):
    __tablename__ = "Booking"

    id = Column(Integer, primary_key=True, index=True)
    passengerId = Column(Integer, ForeignKey("Passenger.id"), nullable=False)
    couponId = Column(Integer, ForeignKey("Coupon.id"), unique=True)
    routeId = Column(Integer, ForeignKey("Routes.id"), nullable=False)
    bookingStatus = Column(String, nullable=False)
