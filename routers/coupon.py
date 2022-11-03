from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from schemas import Createcoupon, Showcoupon
from models import Coupon
from sqlalchemy.orm import Session
from config import setting
from datetime import datetime

router = APIRouter()


@router.post(
    "/coupon",
    tags=["Coupons"],
    response_model=Showcoupon,
    status_code=status.HTTP_201_CREATED,
)
def create_coupon(ref: Createcoupon, db: Session = Depends(get_db)):
    coupon = Coupon(**ref.dict())
    coupon.Issue_date = datetime.now().date()
    db.add(coupon)
    db.commit()
    db.refresh(coupon)
    return coupon
    # return {"message": f"Coupon with id {coupon.id} has been successfully created"}


@router.delete("/coupons/coupon/{id}", tags=["Coupons"])
def delete_coupon_by_id(id: int, db: Session = Depends(get_db)):
    existing_coupon = db.query(Coupon).filter(Coupon.id == id)
    if not existing_coupon.first():
        return {"message": f"No Details found for Coupon ID {id}"}
    existing_coupon.delete()
    db.commit()
    return {"message": f"Coupon ID {id} has been successfully deleted"}
