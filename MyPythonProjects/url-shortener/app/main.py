from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database import engine, Base
from app.routers import stats, links


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="URL Shortener API",
    description="Shorten URLs and track per-link analytics including country breakdown.",
    version="1.0.0",
    lifespan=lifespan,
)

# stats router first so /{code}/stats is evaluated before /{code}
app.include_router(stats.router)
app.include_router(links.router)
