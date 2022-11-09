from fastapi import Depends, HTTPException, status
from database import get_db
from schemas import Createflight
from models import Flights
from sqlalchemy.orm import Session


def createFlight(ref: Createflight, db: Session = Depends(get_db)):
    flight = Flights(**ref.dict())
    db.add(flight)
    db.commit()
    db.refresh(flight)
    return flight


def deleteFlightById(id: int, db: Session = Depends(get_db)):
    existing_flight = db.query(Flights).filter(Flights.id == id)
    if not existing_flight.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Details found for Flight ID {id}",
        )

    existing_flight.delete()
    db.commit()
    return {"message": f"Flight ID {id} has been successfully deleted"}
