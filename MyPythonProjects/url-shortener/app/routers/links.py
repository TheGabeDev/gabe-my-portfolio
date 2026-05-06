import secrets
import string
from datetime import datetime, UTC

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Link, Visit
from app.schemas import ShortenRequest, ShortenResponse
from app.services.ipinfo import get_country

router = APIRouter()

_ALPHABET = string.ascii_letters + string.digits
_CODE_LENGTH = 7


def _generate_code() -> str:
    return "".join(secrets.choice(_ALPHABET) for _ in range(_CODE_LENGTH))


@router.post("/shorten", response_model=ShortenResponse, status_code=201)
async def shorten_url(
    body: ShortenRequest,
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> ShortenResponse:
    for _ in range(5):
        code = _generate_code()
        result = await db.execute(select(Link).where(Link.code == code))
        if result.scalar_one_or_none() is None:
            break
    else:
        raise HTTPException(status_code=500, detail="Could not generate a unique short code")

    link = Link(code=code, original_url=str(body.url))
    db.add(link)
    await db.commit()
    await db.refresh(link)

    base_url = str(request.base_url).rstrip("/")
    return ShortenResponse(
        short_code=code,
        short_url=f"{base_url}/{code}",
        original_url=str(body.url),
    )


@router.get("/{code}")
async def redirect_to_url(
    code: str,
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> RedirectResponse:
    result = await db.execute(select(Link).where(Link.code == code))
    link = result.scalar_one_or_none()
    if link is None:
        raise HTTPException(status_code=404, detail="Short code not found")

    client_ip = request.client.host if request.client else "unknown"
    country = await get_country(client_ip)

    link.last_accessed = datetime.now(UTC)
    db.add(Visit(link_id=link.id, country=country))
    await db.commit()

    return RedirectResponse(url=link.original_url, status_code=301)
