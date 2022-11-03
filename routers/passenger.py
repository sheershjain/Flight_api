from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from schemas import Createuser, Showuser
from models import Passenger
from sqlalchemy.orm import Session
from config import setting
from hashing import Hasher

router = APIRouter()


@router.post(
    "/register",
    tags=["Register"],
    response_model=Showuser,
    status_code=status.HTTP_201_CREATED,
)
def create_passenger(ref: Createuser, db: Session = Depends(get_db)):
    User = Passenger(**ref.dict())
    User.Password = Hasher.get_password_hash(User.Password)
    db.add(User)
    db.commit()
    db.refresh(User)
    return User
    # return {"message": f"Passenger with id {User.id} has been successfully created"}


@router.delete("/register/delete/{id}", tags=["Register"])
def delete_passenger_by_id(id: int, db: Session = Depends(get_db)):
    existing_User = db.query(Passenger).filter(Passenger.id == id)
    if not existing_User.first():
        return {"message": f"No Details found for Passenger ID {id}"}
    existing_User.delete()
    db.commit()
    return {"message": f"Passenger ID {id} has been successfully deleted"}
