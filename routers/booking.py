from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from schemas import Createbooking, Showbooking
from models import Booking, Passenger, Payment, Routes, Flights, Location
from sqlalchemy.orm import Session
from config import setting
from datetime import datetime

router = APIRouter()


@router.post(
    "/Booking",
    tags=["Booking"],
    response_model=Showbooking,
    status_code=status.HTTP_201_CREATED,
)
def create_booking(ref: Createbooking, db: Session = Depends(get_db)):
    obj1 = db.query(Passenger).filter(Passenger.id == ref.Passenger_id)
    if not obj1.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Passenger with id {ref.Passenger_id} not exist. Kindly register the passenger first !",
        )

    obj2 = db.query(Routes).filter(Routes.id == ref.Route_id)
    if not obj2.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Route with id {ref.Route_id} not exist. Kindly create the route first !!",
        )
    obj4 = db.query(Flights).filter(Flights.id == ref.Flight_id)
    if not obj4.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Flight with id {ref.Flight_id} not exist. Kindly create the Flight first !!",
        )

    obj3 = db.query(Payment).filter(Payment.id == ref.Transaction_id)
    if not obj3.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with id {ref.Transaction_id} not exist. Kindly proceed to payment first !",
        )

    booking = Booking(**ref.dict())
    l1 = db.query(Location).filter(Location.id == obj2.first().Source_city_id).first()
    l2 = (
        db.query(Location)
        .filter(Location.id == obj2.first().Destination_city_id)
        .first()
    )

    
    booking.Name = obj1.first().Name
    booking.Email = obj1.first().Email
    booking.Contact_no = obj1.first().Contact_no
    booking.Airlines_name = obj4.first().Airlines_name
    booking.Flight_name = obj4.first().Aeroplane_name
    booking.Amount_paid = obj3.first().Final_amount
    booking.Coupon_status = obj3.first().Coupon_status
    booking.Destination_city_name = l2.City_name
    booking.Source_city_name = l1.City_name
    booking.Address = obj1.first().Address
    booking.Payment_mode = obj3.first().Payment_mode
    booking.Date = datetime.now()
    booking.Status = "Booked"
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking
    # return {"message": f"Booking with id {booking.id} has been successfully created"}


@router.delete("/Booking/delete/{id}", tags=["Booking"])
def delete_booking_by_id(id: int, db: Session = Depends(get_db)):
    existing_booking = db.query(Booking).filter(Booking.id == id)
    if not existing_booking.first():
        return {"message": f"No Details found for Booking ID {id}"}
    existing_booking.delete()
    db.commit()
    return {"message": f"Booking ID {id} has been successfully deleted"}
