from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from schemas import Createlocation, Showlocation
from models import Location
from sqlalchemy.orm import Session
from config import setting

router = APIRouter()


@router.post(
    "/location",
    tags=["Location"],
    response_model=Showlocation,
    status_code=status.HTTP_201_CREATED,
)
def create_location(ref: Createlocation, db: Session = Depends(get_db)):
    location = Location(**ref.dict())
    db.add(location)
    db.commit()
    db.refresh(location)
    return location
    # return {"message": f"Flight with id {flight.id} has been successfully created"}


@router.delete("/location/delete/{id}", tags=["Location"])
def delete_location_by_id(id: int, db: Session = Depends(get_db)):
    existing_location = db.query(Location).filter(Location.id == id)
    if not existing_location.first():
        return {"message": f"No Details found for Location ID {id}"}
    existing_location.delete()
    db.commit()
    return {"message": f"Location ID {id} has been successfully deleted"}
