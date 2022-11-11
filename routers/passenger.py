from fastapi import APIRouter, Depends, status
from db.database import get_db
from db.schemas.Passenger import Createuser, Showuser
from db.models.Passenger import Passenger
from sqlalchemy.orm import Session
from functions.passengerFun import (
    createPassengerFun,
    deletePassengerFun,
    getAllPassengersFun,
)
from typing import List

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
def deletePassengerRoute(id: int, db: Session = Depends(get_db)):
    User = deletePassengerFun(id=id, db=db)
    return User


@router.get(
    "/passenger",
    response_model=List[Showuser],
    tags=["Register"],
    status_code=status.HTTP_200_OK,
)
def getPassengersRoute(db: Session = Depends(get_db)):
    passenger = getAllPassengersFun(db=db)
    return passenger
