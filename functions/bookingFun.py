from fastapi import Depends, HTTPException, status
from db.database import get_db
from db.schemas.Booking import Createbooking, Showbookings
from db.models.Booking import Booking
from db.models.Passenger import Passenger
from db.models.Coupon import Coupon
from db.models.Routes import Routes
from db.models.Payment import Payment
from db.models.Flights import Flights
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime


def bookingOutput(id: int, db: Session):
    booking = db.query(Booking).get(id)
    passenger = db.query(Passenger).get(booking.passengerId)
    route = db.query(Routes).get(booking.routeId)
    flight = db.query(Flights).get(route.flightId)

    object = Showbookings(
        id=booking.id,
        passengerName=passenger.name,
        passengerEmail=passenger.email,
        contactNo=passenger.contactNo,
        aeroplaneName=flight.aeroplaneName,
        airlinesName=flight.airlinesName,
        sourceCityName=route.sourceCityName,
        destinationCityName=route.destinationCityName,
        amount=route.amount,
        bookingDate=booking.bookingDate,
        bookingStatus=booking.bookingStatus,
    )
    return object


def createBookingFun(ref: Createbooking, db: Session = Depends(get_db)):
    passengerObject = db.query(Passenger).filter(Passenger.id == ref.passengerId)
    if not passengerObject.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Passenger with id {ref.passengerId} not exist. Kindly register the passenger first !",
        )

    routeObject = db.query(Routes).filter(Routes.id == ref.routeId)
    if not routeObject.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Route with id {ref.routeId} not exist. Kindly create the route first !!",
        )
    if ref.couponId != None:
        couponObject = db.query(Coupon).filter(Coupon.id == ref.couponId)
        if not couponObject.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Coupon with id {ref.couponId} not exist. Kindly proceed to payment first !",
            )

    booking = Booking(**ref.dict())
    booking.bookingStatus = "Not Booked"
    booking.bookingDate = datetime.now()
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


def deleteBookingFun(id: int, db: Session = Depends(get_db)):
    existing_booking = db.query(Booking).filter(Booking.id == id)
    if not existing_booking.first():
        return {"message": f"No Details found for Booking ID {id}"}
    existing_booking.delete()
    db.commit()
    return {"message": f"Booking ID {id} has been successfully deleted"}


def getBookingFun(db: Session = Depends(get_db)):
    list = []
    existing_booking = db.query(Booking).all()
    if not existing_booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Bookings found",
        )
    for booking in existing_booking:
        object = bookingOutput(booking.id, db)
        list.append(object)
    return list


def getBookingIdFun(id: int, db: Session):
    booking = bookingOutput(id, db)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Bookings found",
        )
    return booking
