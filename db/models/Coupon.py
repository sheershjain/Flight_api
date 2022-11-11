from sqlalchemy import Column, Integer, String, Date, ForeignKey
from db.database import Base


class Coupon(Base):
    __tablename__ = "Discount"

    id = Column(Integer, primary_key=True, index=True)
    couponNo = Column(String, nullable=False)
    couponValue = Column(String, nullable=False)
    issueDate = Column(Date, nullable=False)
    amount = Column(Integer, nullable=False)
