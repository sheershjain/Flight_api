from fastapi import Depends, HTTPException, status
from database import get_db
from schemas import Createbooking, Showbooking
from models import Booking, Passenger, Routes, Flights, Coupon
from sqlalchemy.orm import Session
from typing import List


def bookingOutput(id: int, db: Session):
    booking = db.query(Booking).get(id)
    passenger = db.query(Passenger).get(booking.passengerId)
    route = db.query(Routes).get(booking.routeId)
    flight = db.query(Flights).get(route.flightId)

    object = Showbooking(
        id=booking.id,
        passengerName=passenger.name,
        passengerEmail=passenger.email,
        contactNo=passenger.contactNo,
        aeroplaneName=flight.aeroplaneName,
        airlinesName=flight.airlinesName,
        sourceCityName=route.sourceCityName,
        destinationCityName=route.destinationCityName,
        amount=route.amount,
        bookingStatus=booking.bookingStatus,
    )
    return object


def createBookingFun(ref: Createbooking, db: Session = Depends(get_db)):
    obj1 = db.query(Passenger).filter(Passenger.id == ref.passengerId)
    if not obj1.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Passenger with id {ref.passengerId} not exist. Kindly register the passenger first !",
        )

    obj2 = db.query(Routes).filter(Routes.id == ref.routeId)
    if not obj2.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Route with id {ref.routeId} not exist. Kindly create the route first !!",
        )

    obj3 = db.query(Coupon).filter(Coupon.id == ref.couponId)
    if not obj3.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with id {ref.couponId} not exist. Kindly proceed to payment first !",
        )

    booking = Booking(**ref.dict())
    booking.bookingStatus = "Not Booked"
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
