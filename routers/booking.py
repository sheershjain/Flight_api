from fastapi import APIRouter, Depends, status
from db.database import get_db
from db.schemas.Booking import Createbooking, Showbookings, Showbooking
from sqlalchemy.orm import Session
from typing import List
from functions.bookingFun import (
    createBookingFun,
    deleteBookingFun,
    getBookingFun,
    getBookingIdFun,
)

router = APIRouter()


@router.post(
    "/Booking",
    tags=["Booking"],
    response_model=Showbooking,
    status_code=status.HTTP_201_CREATED,
)
def createBookingRoute(ref: Createbooking, db: Session = Depends(get_db)):
    booking = createBookingFun(ref=ref, db=db)
    return booking


@router.delete("/Booking/delete/{id}", tags=["Booking"])
def deleteBookingRoute(id: int, db: Session = Depends(get_db)):
    booking = deleteBookingFun(id=id, db=db)
    return booking


@router.get("/booking/getAll/", tags=["Booking"], response_model=List[Showbookings])
def getBookingsRoute(db: Session = Depends(get_db)):
    bookings = getBookingFun(db=db)
    return bookings


@router.get(
    "/booking/{id}",
    tags=["Booking"],
    response_model=Showbookings,
    status_code=status.HTTP_200_OK,
)
def getBookingRoute(id: int, db: Session = Depends(get_db)):
    booking = getBookingIdFun(id=id, db=db)
    return booking
