from sqlite3 import version
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')



class Settings:
    title="Flight_api"
    description="""
This API helps you do awesome stuff. 🚀

## Fligts

You can **create and delete Flight details**.

## Routes

You can **create and delete Flight details**.

## Registration

You can register passenger details.

## Coupons

You can create coupon and apply coupon.

## Payment

You can do payment for a flight.
"""
    version="0.0.1"
    terms_of_service="http://example.com/terms/"
    contact={
        "name": "Sheersh Jain",
        "email": "sheersh@gkmit.co",
    }
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
    DATABASE_URL= os.getenv("POSTGRES_URL")
    tags_metadata = [
        {
            "name": "Flights",
            "description": "Operations with Flights.",
        },
        {
            "name": "Routes",
            "description": "Manage routes.",
        },
        {
            "name": "Coupons",
            "description": "Manage coupons.",
        },
        {
            "name": "Payment",
            "description": "Manage Payment for booking.",
        },

    ]
    SECRET_KEY= os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
   
    

    

setting=Settings()