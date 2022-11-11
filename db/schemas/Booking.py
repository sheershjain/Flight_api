from pydantic import BaseModel
from typing import Optional
from datetime import date

class Createbooking(BaseModel):
    passengerId: int
    routeId: int
    couponId: Optional[int] = None


class Showbookings(BaseModel):
    id: int
    passengerName: str
    passengerEmail: str
    amount: int
    contactNo: str
    aeroplaneName: str
    airlinesName: str
    sourceCityName: str
    destinationCityName: str
    bookingDate: date
    bookingStatus: str

    class Config:
        orm_mode = True


class Showbooking(BaseModel):
    id: int
    bookingDate: date
    bookingStatus: str

    class Config:
        orm_mode = True
