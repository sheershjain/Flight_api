from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from schemas import Createflight, Showflight
from models import Flights
from sqlalchemy.orm import Session
from config import setting

router = APIRouter()


@router.post(
    "/flights",
    tags=["Flights"],
    response_model=Showflight,
    status_code=status.HTTP_201_CREATED,
)
def create_flat(ref: Createflight, db: Session = Depends(get_db)):
    flight = Flights(**ref.dict())
    db.add(flight)
    db.commit()
    db.refresh(flight)
    return flight
    # return {"message": f"Flight with id {flight.id} has been successfully created"}


@router.delete("/flights/delete/{id}", tags=["Flights"])
def delete_flat_by_id(id: int, db: Session = Depends(get_db)):
    existing_flight = db.query(Flights).filter(Flights.id == id)
    if not existing_flight.first():
        return {"message": f"No Details found for Flight ID {id}"}
    existing_flight.delete()
    db.commit()
    return {"message": f"Flight ID {id} has been successfully deleted"}
