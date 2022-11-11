from fastapi import Depends, HTTPException, status
from db.database import get_db
from db.schemas.Coupon import Createcoupon
from db.models.Booking import Booking
from db.models.Passenger import Passenger
from db.models.Coupon import Coupon
from db.models.Routes import Routes
from db.models.Payment import Payment
from db.models.Flights import Flights
from sqlalchemy.orm import Session
from datetime import datetime


def createCouponFun(ref: Createcoupon, db: Session = Depends(get_db)):
    coupon = Coupon(**ref.dict())
    coupon.issueDate = datetime.now().date()
    db.add(coupon)
    db.commit()
    db.refresh(coupon)
    return coupon
    # return {"message": f"Coupon with id {coupon.id} has been successfully created"}


def deleteCouponFun(id: int, db: Session = Depends(get_db)):
    existing_coupon = db.query(Coupon).filter(Coupon.id == id)
    if not existing_coupon.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Details found for Coupon ID {id}",
        )
    existing_coupon.delete()
    db.commit()
    return {"message": f"Coupon ID {id} has been successfully deleted"}
