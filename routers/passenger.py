from fastapi import APIRouter, Depends, status
from database import get_db
from schemas import Createuser, Showuser
from models import Passenger
from sqlalchemy.orm import Session
from functions.passengerFun import createPassengerFun, deletePassengerFun

router = APIRouter()


@router.post(
    "/register",
    tags=["Register"],
    response_model=Showuser,
    status_code=status.HTTP_201_CREATED,
)
def createPassengerRoute(ref: Createuser, db: Session = Depends(get_db)):
    User = createPassengerFun(ref=ref, db=db)
    return User


@router.delete("/register/delete/{id}", tags=["Register"])
def delete_passenger_by_id(id: int, db: Session = Depends(get_db)):
    User = deletePassengerFun(id=id, db=db)
    return User
