from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class Createflight(BaseModel):
    aeroplaneName: str
    airlinesName: str
    seatCapacity: int
    availableSeats: int
    totalClass: int
    modelNo: str
    serialNo: str


class Showflight(BaseModel):
    id: int
    aeroplaneName: str
    airlinesName: str
    seatCapacity: int
    availableSeats: int
    totalClass: int
    modelNo: str
    serialNo: str

    class Config:
        orm_mode = True


class Createroute(BaseModel):
    sourceCityName: str
    destinationCityName: str
    flightId: int
    amount: int
    startingTime: str
    endingTime: str


class Showroute(BaseModel):
    id: int
    flightName: str
    amount: int
    startingTime: str
    endingTime: str

    class Config:
        orm_mode = True


class Createuser(BaseModel):
    name: str
    email: EmailStr
    contactNo: str
    address: str
    age: int


class Showuser(BaseModel):
    id: int
    name: str
    email: EmailStr
    contactNo: str
    address: str
    age: int

    class Config:
        orm_mode = True


class Createcoupon(BaseModel):
    couponNo: str
    couponValue: str
    amount: int


class Showcoupon(BaseModel):
    id: int
    couponNo: str
    couponValue: str
    amount: int
    issueDate: date

    class Config:
        orm_mode = True


class Createpayment(BaseModel):
    bankName: str
    bookingId: int
    paymentMode: str


class Showpayment(BaseModel):
    id: int
    bankName: str
    paymentMode: str
    date: date
    amount: int
    couponStatus: str
    finalAmount: int
    paymentStatus: str

    class Config:
        orm_mode = True


class Createbooking(BaseModel):
    passengerId: int
    routeId: int
    couponId: Optional[int] = None


class Showbooking(BaseModel):
    id: int
    passengerName: str
    passengerEmail: str
    amount: int
    contactNo: str
    aeroplaneName: str
    airlinesName: str
    sourceCityName: str
    destinationCityName: str
    bookingStatus: str

    class Config:
        orm_mode = True
