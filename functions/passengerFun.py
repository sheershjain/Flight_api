from fastapi import Depends, HTTPException, status
from db.database import get_db
from db.schemas.Passenger import Createuser
from db.models.Booking import Booking
from db.models.Passenger import Passenger
from db.models.Coupon import Coupon
from db.models.Routes import Routes
from db.models.Payment import Payment
from db.models.Flights import Flights
from sqlalchemy.orm import Session


def createPassengerFun(ref: Createuser, db: Session = Depends(get_db)):
    User = Passenger(**ref.dict())
    db.add(User)
    db.commit()
    db.refresh(User)
    return User


def deletePassengerFun(id: int, db: Session = Depends(get_db)):
    existing_User = db.query(Passenger).filter(Passenger.id == id)
    if not existing_User.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Details found for Passenger ID {id}",
        )
    existing_User.delete()
    db.commit()
    return {"message": f"Passenger ID {id} has been successfully deleted"}


def getAllPassengersFun(db: Session):
    passenger = db.query(Passenger).all()
    if not passenger:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Passengers found",
        )
    return passenger
