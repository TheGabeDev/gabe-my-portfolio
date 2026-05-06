import os
import httpx
from dotenv import load_dotenv

load_dotenv()

IPINFO_TOKEN = os.getenv("IPINFO_TOKEN", "")
_LOCAL_IPS = {"127.0.0.1", "::1", "testclient", "localhost"}


async def get_country(ip: str) -> str | None:
    if ip in _LOCAL_IPS:
        return None
    try:
        params = {"token": IPINFO_TOKEN} if IPINFO_TOKEN else {}
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(f"https://ipinfo.io/{ip}/json", params=params)
            response.raise_for_status()
            return response.json().get("country")
    except Exception:
        return None
