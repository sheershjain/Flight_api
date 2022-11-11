from pydantic import BaseModel


class Createflight(BaseModel):
    aeroplaneName: str
    airlinesName: str
    seatCapacity: int
    totalClass: int
    modelNo: str
    serialNo: str


class Showflight(BaseModel):
    id: int
    aeroplaneName: str
    airlinesName: str
    seatCapacity: int
    totalClass: int
    modelNo: str
    serialNo: str

    class Config:
        orm_mode = True
