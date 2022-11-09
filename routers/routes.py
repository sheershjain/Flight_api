from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from schemas import Createroute,Showroute
from models import Routes, Flights
from sqlalchemy.orm import Session
from config import setting
from typing import List

router = APIRouter()


@router.post("/routes", tags=["Routes"], status_code=status.HTTP_201_CREATED)
def create_route(ref: Createroute, db: Session = Depends(get_db)):
    if ref.Source_city_name==ref.Destination_city_name:
        return {
            "message": "Source and destination city can't be same"
        }
    flight=db.query(Flights).filter(Flights.id==ref.Flight_id)
    if not flight.first():
        return {"message": f"Flight id {ref.Flight_id} do not exist "}
    name=flight.first().Aeroplane_name
    routes = Routes(**ref.dict())
    routes.Source_city_name=ref.Source_city_name.lower()
    routes.Destination_city_name=ref.Destination_city_name.lower()
    routes.Flight_name=name
    db.add(routes)
    db.commit()
    db.refresh(routes)
    # return routes

    return {
        "message": f"Route with id {routes.id} [ {ref.Source_city_name.upper()} - {ref.Destination_city_name.upper()} ] has been successfully created"
    }
    # return {"message": "Route with id   has been successfully created"}


@router.delete("/routes/delete/{id}", tags=["Routes"])
def delete_route_by_id(id: int, db: Session = Depends(get_db)):
    existing_routes = db.query(Routes).filter(Routes.id == id)
    if not existing_routes.first():
        return {"message": f"No Details found for Route ID {id}"}
    existing_routes.delete()
    db.commit()
    return {"message": f"Route with ID {id} has been successfully deleted"}

@router.get("/routes/get/{source_city}/{destination_city}", tags=["Routes"],response_model=List[Showroute])
def get_route_by_city(source_city: str,destination_city:str ,db: Session = Depends(get_db)):
    if source_city==destination_city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Source and destination city can't be same ",
        )
        
    existing_routes = db.query(Routes).filter(Routes.Source_city_name == source_city.lower() , Routes.Destination_city_name == destination_city.lower()).all()
    if not existing_routes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Route found",
        )
        
    return existing_routes
    