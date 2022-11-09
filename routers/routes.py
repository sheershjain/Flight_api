from fastapi import APIRouter, Depends, status
from database import get_db
from schemas import Createroute, Showroute
from sqlalchemy.orm import Session
from typing import List
from functions.routesFun import createRouteFun, deleteRouteFun, getRouteFun

router = APIRouter()


@router.post("/routes", tags=["Routes"], status_code=status.HTTP_201_CREATED)
def createRoute(ref: Createroute, db: Session = Depends(get_db)):
    route = createRouteFun(ref=ref, db=db)
    return route


@router.delete(
    "/routes/delete/{id}",
    tags=["Routes"],
)
def deleteRoute(id: int, db: Session = Depends(get_db)):
    route = deleteRouteFun(id=id, db=db)
    return route


@router.get(
    "/routes/get/{source_city}/{destination_city}",
    tags=["Routes"],
    response_model=List[Showroute],
)
def getRoute(source_city: str, destination_city: str, db: Session = Depends(get_db)):
    route = getRouteFun(
        source_city=source_city, destination_city=destination_city, db=db
    )
    return route
