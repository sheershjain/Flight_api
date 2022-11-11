from pydantic import BaseModel


class Createroute(BaseModel):
    sourceCityName: str
    destinationCityName: str
    flightId: int
    amount: int
    startingTime: str
    endingTime: str


class Showroute(BaseModel):
    id: int
    flightName: str
    amount: int
    startingTime: str
    endingTime: str

    class Config:
        orm_mode = True
