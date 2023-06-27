from fastapi import FastAPI

from src.auth.router import router as auth_router
from src.booking.router import router as booking_router

app = FastAPI(redoc_url=None)

app.include_router(auth_router)
app.include_router(booking_router)
