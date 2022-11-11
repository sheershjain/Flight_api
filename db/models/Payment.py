from sqlalchemy import Column, Integer, String, Date, ForeignKey
from db.database import Base


class Payment(Base):
    __tablename__ = "Transaction"

    id = Column(Integer, primary_key=True, index=True)
    bankName = Column(String, nullable=False)
    paymentMode = Column(String, nullable=False)
    bookingId = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    amount = Column(Integer, nullable=False)
    couponStatus = Column(String)
    finalAmount = Column(Integer)
    paymentStatus = Column(String)
