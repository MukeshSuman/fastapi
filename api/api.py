from fastapi import APIRouter

from api.endpoints import contact_us, send_email, demo

api_router = APIRouter()
api_router.include_router(contact_us.router,
                          prefix="/contact_us",
                          tags=["Contact Us"])
api_router.include_router(demo.router, prefix="/demo", tags=["Demo"])
api_router.include_router(send_email.router,
                          prefix="/send_email",
                          tags=["Send Email"])
