from pydantic import BaseModel, EmailStr


class Createuser(BaseModel):
    name: str
    email: EmailStr
    contactNo: str
    address: str
    age: int


class Showuser(BaseModel):
    id: int
    name: str
    email: EmailStr
    contactNo: str
    address: str
    age: int

    class Config:
        orm_mode = True
