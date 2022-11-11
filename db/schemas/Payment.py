from pydantic import BaseModel
from datetime import date


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
