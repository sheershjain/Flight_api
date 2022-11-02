from sqlite3 import version
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")


class Settings:
    title = "Flight_api"
    description = """
This API helps you do awesome stuff. 🚀

## Flights

You can **create and delete Flight details**.

## Routes

You can **create and delete Flight details**.

## Location

You can **create and delete Location details**.

## Registration

You can register passenger details.

## Coupons

You can create coupon and apply coupon.

## Payment

You can do payment for a flight.

Steps to follow:
1. Register the passenger
2. Create Location1
3. Create Location2
4. Create Route for the previously created locations
5. Create Coupon
6. Apply coupon and do payment
7. Book the flight


"""
    version = "0.0.1"
    terms_of_service = "http://example.com/terms/"
    contact = {
        "name": "Sheersh Jain",
        "email": "sheersh@gkmit.co",
    }
    license_info = {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
    DATABASE_URL = os.getenv("POSTGRES_URL")
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
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"


setting = Settings()
