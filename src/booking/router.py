from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.auth import current_active_user
from src.auth.models import User
from src.booking.models import apartment, booking
from src.booking.schemas import Apartment, ApartmentCreate, UserApartments, BookingCreate, BookingRead
from src.database import get_async_session

router = APIRouter(
    prefix="/apartment",
    tags=['Apartment']
)


@router.get("/list/{city}", response_model=list[Apartment])
async def apartment_list_route(city: int, session: AsyncSession = Depends(get_async_session)):
    query = select(apartment).where(apartment.c.city_id == city)
    result = await session.execute(query)
    return result.all()


@router.post("/create")
async def apartment_create_route(
        new_apartment: ApartmentCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user),
):
    try:
        new_apartment.user_id = user.id
        stmt = insert(apartment).values(**new_apartment.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as e22:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.get("/user-apartments", response_model=list[UserApartments])
async def current_user_apartment_list_route(
        user: User = Depends(current_active_user),
        session: AsyncSession = Depends(get_async_session)
):
    try:
        query = select(apartment).where(apartment.c.user_id == user.id)
        result = await session.execute(query)
        return result.all()
    except Exception:
        raise HTTPException(status_code=403, detail={
            "status": "error",
            "data": None,
            "details": None
        })



@router.post("/booking/create")
async def current_user_booking_list_route(
        new_booking: BookingCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_active_user),
):
    try:
        new_booking.user_id = user.id
        stmt = insert(booking).values(**new_booking.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception:
        raise HTTPException(status_code=403, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.get("/booking/current-user-list", response_model=list[BookingRead])
async def current_user_booking_list_route(
        user: User = Depends(current_active_user),
        session: AsyncSession = Depends(get_async_session)
):
    try:
        query = select(booking).where(booking.c.user_id == user.id)
        results = await session.execute(query)
        return results.all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=403, detail={
            "status": "Error",
            "data": None,
            "details": None
        })


@router.get("/booking/apartment/{apartment_id}", response_model=list[BookingRead])
async def current_user_booking_list_route(
        apartment_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        query = select(booking).where(booking.c.apartment_id == apartment_id)
        results = await session.execute(query)
        return results.all()
    except Exception:
        raise HTTPException(status_code=404, detail={
            "status": "Error",
            "data": None,
            "details": None
        })