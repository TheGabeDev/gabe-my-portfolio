from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Link, Visit
from app.schemas import StatsResponse

router = APIRouter()


@router.get("/{code}/stats", response_model=StatsResponse)
async def get_stats(code: str, db: AsyncSession = Depends(get_db)) -> StatsResponse:
    result = await db.execute(select(Link).where(Link.code == code))
    link = result.scalar_one_or_none()
    if link is None:
        raise HTTPException(status_code=404, detail="Short code not found")

    visits_result = await db.execute(select(Visit).where(Visit.link_id == link.id))
    visits = visits_result.scalars().all()

    country_breakdown: dict[str, int] = {}
    for visit in visits:
        key = visit.country or "unknown"
        country_breakdown[key] = country_breakdown.get(key, 0) + 1

    return StatsResponse(
        short_code=link.code,
        original_url=link.original_url,
        click_count=len(visits),
        created_at=link.created_at,
        last_accessed=link.last_accessed,
        country_breakdown=country_breakdown,
    )
