from fastapi import APIRouter, Depends, status
from database import get_db
from schemas import Createcoupon, Showcoupon
from sqlalchemy.orm import Session
from functions.couponFun import createCouponFun, deleteCouponFun

router = APIRouter()


@router.post(
    "/coupon",
    tags=["Coupons"],
    response_model=Showcoupon,
    status_code=status.HTTP_201_CREATED,
)
def createCouponRoute(ref: Createcoupon, db: Session = Depends(get_db)):
    coupon = createCouponFun(ref=ref, db=db)
    return coupon


@router.delete("/coupons/coupon/{id}", tags=["Coupons"])
def deleteCouponRoute(id: int, db: Session = Depends(get_db)):
    coupon = deleteCouponFun(id=id, db=db)
    return coupon
