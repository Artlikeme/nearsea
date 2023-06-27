from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.booking.models import apartment
from src.booking.schemas import ApartmentList, ApartmentCreate
from src.database import get_async_session

router = APIRouter(
    prefix="/apartment",
    tags=['Apartment']
)


@router.get("/list", response_model=list[ApartmentList])
async def apartment_list_route(session: AsyncSession = Depends(get_async_session)):
    query = select(apartment)
    result = await session.execute(query)
    return result.all()


@router.post("/create")
async def apartment_create_route(
        new_apartment: ApartmentCreate,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        stmt = insert(apartment).values(**new_apartment.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })