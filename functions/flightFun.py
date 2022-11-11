from fastapi import Depends, HTTPException, status
from db.database import get_db
from db.schemas.Flights import Createflight
from db.models.Booking import Booking
from db.models.Passenger import Passenger
from db.models.Coupon import Coupon
from db.models.Routes import Routes
from db.models.Payment import Payment
from db.models.Flights import Flights
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


def getAllFlightsFun(db: Session):
    flights = db.query(Flights).all()
    if not flights:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Flights found",
        )
    return flights
