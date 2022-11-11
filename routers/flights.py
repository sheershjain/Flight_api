from fastapi import APIRouter, Depends, status
from db.database import get_db
from db.schemas.Flights import Createflight, Showflight
from sqlalchemy.orm import Session
from functions.flightFun import createFlight, deleteFlightById, getAllFlightsFun
from typing import List

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


@router.get(
    "/flights",
    response_model=List[Showflight],
    tags=["Flights"],
    status_code=status.HTTP_200_OK,
)
def getFlightsRoute(db: Session = Depends(get_db)):
    flights = getAllFlightsFun(db=db)
    return flights
