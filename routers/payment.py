from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from schemas import Createpayment, Showpayment
from models import Payment, Coupon, Routes
from sqlalchemy.orm import Session
from config import setting
from datetime import datetime

router = APIRouter()


@router.post(
    "/payment",
    tags=["Payment"],
    response_model=Showpayment,
    status_code=status.HTTP_201_CREATED,
)
def create_payment(ref: Createpayment, db: Session = Depends(get_db)):
    payment = Payment(**ref.dict())
    payment.Date = datetime.now()
    Route=db.query(Routes).filter(Routes.id==ref.Route_id)
    if not Route:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Route id {ref.Route_id} do not exist",
        )
    payment.Amount=Route.first().Amount
    obj = db.query(Coupon).filter(Coupon.id == ref.Coupon_id)
    if obj.first():
        am = payment.Amount - obj.first().Amount
        payment.Coupon_status = "Applied"
        payment.Final_amount = am
    else:
        payment.Coupon_status = "Not Applied"
        payment.Final_amount = payment.Amount
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment
    # return {"message": f"payment with id {payment.id} has been successfully created"}


@router.delete("/payment/delete/{id}", tags=["Payment"])
def delete_payment_by_id(id: int, db: Session = Depends(get_db)):
    existing_payment = db.query(Payment).filter(Payment.id == id)
    if not existing_payment.first():
        return {"message": f"No Details found for payment ID {id}"}
    existing_payment.delete()
    db.commit()
    return {"message": f"Payment with ID {id} has been successfully deleted"}
