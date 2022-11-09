from enum import unique
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base


class Flights(Base):
    __tablename__ = "Flights"

    id = Column(Integer, primary_key=True, index=True)
    Aeroplane_name = Column(String, nullable=False, unique=True)
    Airlines_name = Column(String, nullable=False)
    seat_capacity = Column(Integer, nullable=False, unique=True)
    total_class = Column(Integer, nullable=False)
    model_no = Column(String, nullable=False, unique=True)
    serial_no = Column(String, nullable=False, unique=True)


class Routes(Base):
    __tablename__ = "Routes"

    id = Column(Integer, primary_key=True, index=True)
    Source_city_name = Column(String)
    Destination_city_name = Column(String)
    Flight_name = Column(String,nullable=False)
    Flight_id = Column(Integer,nullable=False)
    Amount = Column(Integer,nullable=False)
    Starting_time = Column(String,nullable=False)
    Ending_time = Column(String,nullable=False)


# class Location(Base):
#     __tablename__ = "Location"

#     id = Column(Integer, primary_key=True, index=True)
#     Pincode = Column(String, nullable=False)
#     City_name = Column(String, nullable=False)
#     State = Column(String, nullable=False)


class Passenger(Base):
    __tablename__ = "Passenger"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    Contact_no = Column(String, nullable=False)
    Address = Column(String, nullable=False)
    Age = Column(Integer, nullable=False)
    Password = Column(String, nullable=False)


class Coupon(Base):
    __tablename__ = "Discount"

    id = Column(Integer, primary_key=True, index=True)
    Coupon_no = Column(String, nullable=False)
    Coupon_value = Column(String, nullable=False)
    Issue_date = Column(Date, nullable=False)
    Amount = Column(Integer, nullable=False)


class Payment(Base):
    __tablename__ = "Transaction"

    id = Column(Integer, primary_key=True, index=True)
    Bank_name = Column(String, nullable=False)
    Payment_mode = Column(String, nullable=False)
    Route_id = Column(Integer,nullable=False)
    Date = Column(Date, nullable=False)
    Coupon_id = Column(String, ForeignKey("Discount.id"))
    Amount = Column(Integer, nullable=False)
    Coupon_status = Column(String)
    Final_amount = Column(Integer)
    





# class Booking(Base):
#     __tablename__ = "Booking"

#     id = Column(Integer, primary_key=True, index=True)
#     Name = Column(String, nullable=False)
#     Contact_no = Column(String, nullable=False)
#     Email = Column(String, nullable=False)
#     Address = Column(String, nullable=False)
#     Source_city_name = Column(String, nullable=False)
#     Destination_city_name = Column(String, nullable=False)
#     Flight_name = Column(String, nullable=False)
#     Coupon_status = Column(String, nullable=False)
#     Amount_paid = Column(Integer, nullable=False)
#     Payment_mode = Column(String, nullable=False)
#     Passenger_id = Column(Integer, nullable=False)
#     Transaction_id = Column(Integer, nullable=False)
#     Route_id = Column(Integer, nullable=False)
#     Date = Column(Date, nullable=False)
#     Status = Column(String, nullable=False)

class Booking(Base):
    __tablename__ = "Booking"

    id = Column(Integer, primary_key=True, index=True)
    Passenger_id = Column(Integer, nullable=False)
    Transaction_id = Column(Integer, nullable=False)
    Route_id = Column(Integer, nullable=False)
    Status = Column(String, nullable=False)

