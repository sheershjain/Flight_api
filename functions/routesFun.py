from fastapi import Depends, HTTPException, status
from db.database import get_db
from db.schemas.Routes import Createroute, Showroute
from db.models.Booking import Booking
from db.models.Passenger import Passenger
from db.models.Coupon import Coupon
from db.models.Routes import Routes
from db.models.Payment import Payment
from db.models.Flights import Flights
from sqlalchemy.orm import Session


def createRouteFun(ref: Createroute, db: Session = Depends(get_db)):
    if ref.sourceCityName == ref.destinationCityName:
        return {"message": "Source and destination city can't be same"}
    flight = db.query(Flights).filter(Flights.id == ref.flightId)
    if not flight.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Flight id {ref.flightId} do not exist ",
        )
    routes = Routes(**ref.dict())
    routes.sourceCityName = ref.sourceCityName.lower()
    routes.destinationCityName = ref.destinationCityName.lower()
    db.add(routes)
    db.commit()
    db.refresh(routes)

    return {
        "message": f"Route with id {routes.id} [ {ref.sourceCityName.upper()} - {ref.destinationCityName.upper()} ] has been successfully created"
    }


def deleteRouteFun(id: int, db: Session = Depends(get_db)):
    existing_routes = db.query(Routes).filter(Routes.id == id)
    if not existing_routes.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Details found for Route ID {id}",
        )
    existing_routes.delete()
    db.commit()
    return {"message": f"Route with ID {id} has been successfully deleted"}


def routeOutput(id: int, db: Session):
    obj = db.query(Routes).get(id)
    flight = db.query(Flights).get(obj.flightId)
    object = Showroute(
        id=obj.id,
        flightName=flight.aeroplaneName,
        amount=obj.amount,
        startingTime=obj.startingTime,
        endingTime=obj.endingTime,
    )
    return object


def getRouteFun(source_city: str, destination_city: str, db: Session = Depends(get_db)):
    list = []

    if source_city == destination_city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Source and destination city can't be same ",
        )

    existing_routes = (
        db.query(Routes)
        .filter(
            Routes.sourceCityName == source_city.lower(),
            Routes.destinationCityName == destination_city.lower(),
        )
        .all()
    )

    if not existing_routes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Route found",
        )

    for routes in existing_routes:
        object = routeOutput(routes.id, db)
        list.append(object)
    return list
