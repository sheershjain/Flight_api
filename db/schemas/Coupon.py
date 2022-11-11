from pydantic import BaseModel
from datetime import date


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
