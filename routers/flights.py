from fastapi import APIRouter, Depends, status
from database import get_db
from schemas import Createflight, Showflight
from sqlalchemy.orm import Session
from functions.flightFun import createFlight, deleteFlightById

router = APIRouter()


@router.post(
    "/flights",
    tags=["Flights"],
    response_model=Showflight,
    status_code=status.HTTP_201_CREATED,
)
def createFlightRoute(ref: Createflight, db: Session = Depends(get_db)):
    flight = createFlight(ref=ref, db=db)
    return flight


@router.delete("/flights/delete/{id}", tags=["Flights"])
def deleteFlightRoute(id: int, db: Session = Depends(get_db)):
    flight = deleteFlightById(id=id, db=db)
    return flight
