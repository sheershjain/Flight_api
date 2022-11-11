from fastapi import APIRouter, Depends, HTTPException, status
from db.database import get_db
from db.schemas.Payment import Createpayment
from db.models.Booking import Booking
from db.models.Passenger import Passenger
from db.models.Coupon import Coupon
from db.models.Routes import Routes
from db.models.Payment import Payment
from db.models.Flights import Flights
from sqlalchemy.orm import Session
from config import setting
from datetime import datetime


def createPaymentFun(ref: Createpayment, db: Session = Depends(get_db)):
    payment = Payment(**ref.dict())
    payment.date = datetime.now()
    booking = db.query(Booking).filter(Booking.id == ref.bookingId)
    if not booking.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Booking Id {ref.bookingId} do not exist",
        )
    route = db.query(Routes).filter(Routes.id == booking.first().routeId)
    if not route:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Route Id {booking.first().routeId} do not exist",
        )
    payment.amount = route.first().amount
    obj = db.query(Coupon).filter(Coupon.id == booking.first().couponId)
    if obj.first():
        am = payment.amount - obj.first().amount
        payment.couponStatus = "Applied"
        payment.finalAmount = am
    else:
        payment.couponStatus = "Not Applied"
        payment.finalAmount = payment.amount
    booking.first().bookingStatus = "Booked"
    booking.first().amount = payment.finalAmount
    payment.paymentStatus = "Paid"
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment


def deletePaymentFun(id: int, db: Session = Depends(get_db)):
    existing_payment = db.query(Payment).filter(Payment.id == id)
    if not existing_payment.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Details found for payment ID {id}",
        )
    existing_payment.delete()
    db.commit()
    return {"message": f"Payment with ID {id} has been successfully deleted"}
