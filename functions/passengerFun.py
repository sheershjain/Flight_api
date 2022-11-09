from fastapi import Depends, HTTPException, status
from database import get_db
from schemas import Createuser
from models import Passenger
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
