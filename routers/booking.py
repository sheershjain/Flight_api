from fastapi import APIRouter, Depends, status
from database import get_db
from schemas import Createbooking, Showbooking
from sqlalchemy.orm import Session
from typing import List
from functions.bookingFun import createBookingFun, deleteBookingFun, getBookingFun

router = APIRouter()


@router.post(
    "/Booking",
    tags=["Booking"],
    status_code=status.HTTP_201_CREATED,
)
def createBookingRoute(ref: Createbooking, db: Session = Depends(get_db)):
    booking = createBookingFun(ref=ref, db=db)
    return booking


@router.delete("/Booking/delete/{id}", tags=["Booking"])
def delete_booking_by_id(id: int, db: Session = Depends(get_db)):
    booking = deleteBookingFun(id=id, db=db)
    return booking


@router.get("/booking/getAll/", tags=["Booking"], response_model=List[Showbooking])
def getBookingsRoute(db: Session = Depends(get_db)):
    booking = getBookingFun(db=db)
    return booking
