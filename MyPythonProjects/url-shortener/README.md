# URL Shortener API

A production-style REST API built with **FastAPI** that shortens URLs and tracks per-link analytics — including click counts, timestamps, and a country breakdown of visitors powered by the [IPInfo](https://ipinfo.io) API.

## Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI + Uvicorn |
| Database | SQLite via SQLAlchemy (async) + aiosqlite |
| Validation | Pydantic v2 |
| HTTP client | httpx (IPInfo integration) |
| Tests | pytest + pytest-asyncio |

---

## Setup

```bash
# 1. Clone and enter the project
git clone <repo-url>
cd url-shortener

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env and add your IPINFO_TOKEN (optional but recommended)

# 5. Start the server
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

---

## API Endpoints

### POST /shorten — Create a short link

```bash
curl -X POST http://localhost:8000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/some/very/long/path?with=query&params=true"}'
```

**Response `201 Created`:**
```json
{
  "short_code": "aB3dE7f",
  "short_url": "http://localhost:8000/aB3dE7f",
  "original_url": "https://www.example.com/some/very/long/path?with=query&params=true"
}
```

---

### GET /{code} — Redirect to original URL

```bash
curl -L http://localhost:8000/aB3dE7f
# Follows the 301 redirect to the original URL

# Or inspect the redirect without following it:
curl -I http://localhost:8000/aB3dE7f
```

**Response `301 Moved Permanently`** with `Location` header pointing to the original URL.
Each visit records the requester's country code via IPInfo.

---

### GET /{code}/stats — View link analytics

```bash
curl http://localhost:8000/aB3dE7f/stats
```

**Response `200 OK`:**
```json
{
  "short_code": "aB3dE7f",
  "original_url": "https://www.example.com/some/very/long/path?with=query&params=true",
  "click_count": 3,
  "created_at": "2024-01-15T10:30:00Z",
  "last_accessed": "2024-01-15T11:45:22Z",
  "country_breakdown": {
    "US": 2,
    "DE": 1
  }
}
```

---

## Running Tests

```bash
pytest -v
```

The test suite uses an in-memory SQLite database — no `.env` configuration required.

---

## Project Structure

```
url-shortener/
├── app/
│   ├── main.py          # FastAPI app, lifespan, router registration
│   ├── database.py      # Async SQLAlchemy engine + session factory
│   ├── models.py        # ORM models: Link, Visit
│   ├── schemas.py       # Pydantic v2 request/response schemas
│   ├── routers/
│   │   ├── links.py     # POST /shorten, GET /{code}
│   │   └── stats.py     # GET /{code}/stats
│   └── services/
│       └── ipinfo.py    # Async IPInfo API client
├── tests/
│   ├── conftest.py      # Shared fixtures (in-memory DB, test client)
│   ├── test_links.py    # Shorten + redirect tests
│   └── test_stats.py    # Analytics tests
├── .env.example
├── pyproject.toml       # pytest configuration
└── requirements.txt
```

---

## How It Could Be Extended

| Feature | Approach |
|---|---|
| **Custom aliases** | Add an optional `alias` field to `POST /shorten`; validate uniqueness before insert |
| **Expiring links** | Add an `expires_at` column to `Link`; check it in the redirect handler and return `410 Gone` |
| **Rate limiting** | Add `slowapi` middleware keyed on the client IP to prevent abuse of `POST /shorten` |
| **PostgreSQL** | Swap `DATABASE_URL` to `postgresql+asyncpg://...` and add `asyncpg` to requirements — no code changes needed |
| **Authentication** | Add JWT-based auth with `python-jose`; protect `POST /shorten` and scoped stats behind user ownership |
| **QR codes** | On shorten, generate a QR code with `qrcode` and return a `qr_url` pointing to a stored PNG |
| **Click-through rate UI** | Serve a small React/HTMX dashboard at `/dashboard` consuming the `/stats` endpoints |
| **Caching** | Cache redirect lookups in Redis with a short TTL; invalidate on deletion |

---

## Design Notes

- **301 vs 302:** The redirect uses `301 Moved Permanently`. Browsers may cache this, so subsequent clicks from the same browser won't hit the server (and won't register in analytics). Using `302 Found` would fix that at the cost of slightly worse SEO. The right choice depends on the use case.
- **IPInfo failures are silent:** Network errors or rate-limit responses from IPInfo are caught and stored as `null` country rather than failing the redirect. Availability of the core feature is prioritised over analytics completeness.
- **Code generation:** Short codes are 7 characters from `[a-zA-Z0-9]` (62^7 ≈ 3.5 trillion combinations) generated with `secrets.choice` for cryptographic randomness.
