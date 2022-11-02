from fastapi import FastAPI
from config import setting
from database import engine
from models import Base
from routers import flights, location, routes, passenger, coupon, payment, booking


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=setting.title,
    description=setting.description,
    version=setting.version,
    terms_of_service=setting.terms_of_service,
    contact=setting.contact,
    license_info=setting.license_info,
    openapi_tags=setting.tags_metadata,
)

app.include_router(flights.router)
app.include_router(location.router)
app.include_router(routes.router)
app.include_router(passenger.router)
app.include_router(coupon.router)
app.include_router(payment.router)
app.include_router(booking.router)
