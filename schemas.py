from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class Createflight(BaseModel):
    Aeroplane_name: str
    Airlines_name: str
    seat_capacity: int
    total_class: int
    model_no: str
    serial_no: str


class Showflight(BaseModel):
    id: int
    Aeroplane_name: str
    Airlines_name: str
    seat_capacity: int
    total_class: int
    model_no: str
    serial_no: str

    class Config:
        orm_mode = True


class Createlocation(BaseModel):
    Pincode: str
    Longitude: str
    Lattitude: str
    City_name: str
    State: str


class Showlocation(BaseModel):
    id: int
    Pincode: str
    Longitude: str
    Lattitude: str
    City_name: str
    State: str

    class Config:
        orm_mode = True


class Createroute(BaseModel):
    Source_city_id: int
    Destination_city_id: int


class Showroute(BaseModel):
    id: int
    Source_city_id: str
    Destination_city_id: str

    class Config:
        orm_mode = True


class Createuser(BaseModel):
    Name: str
    Email: EmailStr
    Contact_no: str
    Address: str
    Age: int
    Password: str


class Showuser(BaseModel):
    id: int
    Name: str
    Email: EmailStr
    Contact_no: str
    Address: str
    Age: int

    class Config:
        orm_mode = True


class Createcoupon(BaseModel):
    Coupon_no: str
    Coupon_value: str
    Amount: int


class Showcoupon(BaseModel):
    id: int
    Coupon_no: str
    Coupon_value: str
    Amount: int
    Issue_date: date

    class Config:
        orm_mode = True


class Createpayment(BaseModel):
    Bank_name: str
    Payment_mode: str
    Coupon_id: Optional[int] = None
    Amount: int


class Showpayment(BaseModel):
    id: int
    Bank_name: str
    Payment_mode: str
    Date: date
    Coupon_id: int
    Amount: int
    Coupon_status: str
    Final_amount: int

    class Config:
        orm_mode = True


class Createbooking(BaseModel):
    Passenger_id: int
    Route_id: int
    Flight_id: int
    Transaction_id: int


# class Showbooking(BaseModel):
#     id: int
#     Passenger_id : int
#     Transaction_id : int
#     Route_id : int
#     Flight_id : int
#     Date : date
#     Status : str

#     class Config:
#         orm_mode = True


class Showbooking(BaseModel):
    id: int
    Name: str
    Email: str
    Contact_no: str
    Address: str
    Source_city_name: str
    Destination_city_name: str
    Flight_name: str
    Airlines_name: str
    Coupon_status: str
    Payment_mode: str
    Amount_paid: int

    Date: date
    Status: str

    class Config:
        orm_mode = True
