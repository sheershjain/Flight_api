from fastapi import APIRouter, Depends, status
from db.database import get_db
from db.schemas.Payment import Createpayment, Showpayment
from sqlalchemy.orm import Session
from functions.paymentFun import createPaymentFun, deletePaymentFun

router = APIRouter()


@router.post(
    "/payment",
    tags=["Payment"],
    response_model=Showpayment,
    status_code=status.HTTP_201_CREATED,
)
def createPaymentRoute(ref: Createpayment, db: Session = Depends(get_db)):
    payment = createPaymentFun(ref=ref, db=db)
    return payment


@router.delete("/payment/delete/{id}", tags=["Payment"])
def deletePaymentRoute(id: int, db: Session = Depends(get_db)):
    payment = deletePaymentFun(id=id, db=db)
    return payment
