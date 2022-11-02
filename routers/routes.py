from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from schemas import Createroute
from models import Routes, Location
from sqlalchemy.orm import Session
from config import setting

router = APIRouter()


@router.post("/routes", tags=["Routes"], status_code=status.HTTP_201_CREATED)
def create_flat(ref: Createroute, db: Session = Depends(get_db)):
    obj1 = db.query(Location).filter(Location.id == ref.Source_city_id)
    if not obj1.first():
        return {
            "message": f"Invalid Source city ID {ref.Source_city_id}. Kindly create that location first ! "
        }
    obj2 = db.query(Location).filter(Location.id == ref.Destination_city_id)
    if not obj2.first():
        return {
            "message": f"Invalid Destination city ID {ref.Destination_city_id}. Kindly create that location first ! "
        }
    routes = Routes(**ref.dict())
    db.add(routes)
    db.commit()
    db.refresh(routes)
    # return routes

    return {
        "message": f"Route with id {routes.id} [ {obj1.first().City_name} - {obj2.first().City_name} ] has been successfully created"
    }
    # return {"message": "Route with id   has been successfully created"}


@router.delete("/routes/delete/{id}", tags=["Routes"])
def delete_flat_by_id(id: int, db: Session = Depends(get_db)):
    existing_routes = db.query(Routes).filter(Routes.id == id)
    if not existing_routes.first():
        return {"message": f"No Details found for Route ID {id}"}
    existing_routes.delete()
    db.commit()
    return {"message": f"Route with ID {id} has been successfully deleted"}
