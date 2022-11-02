from fastapi import FastAPI
from config import setting

app = FastAPI(
    title=setting.title,
    description=setting.description,
    version=setting.version,
    terms_of_service=setting.terms_of_service,
    contact=setting.contact,
    license_info=setting.license_info,
    openapi_tags=setting.tags_metadata
)


