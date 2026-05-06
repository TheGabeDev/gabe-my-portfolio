import pytest


@pytest.mark.asyncio
async def test_stats_initial_zero_clicks(client):
    shorten = await client.post("/shorten", json={"url": "https://stats-zero.com"})
    code = shorten.json()["short_code"]

    response = await client.get(f"/{code}/stats")
    assert response.status_code == 200
    data = response.json()
    assert data["short_code"] == code
    assert data["click_count"] == 0
    assert data["last_accessed"] is None
    assert data["country_breakdown"] == {}


@pytest.mark.asyncio
async def test_stats_after_single_click(client):
    shorten = await client.post("/shorten", json={"url": "https://stats-one.com"})
    code = shorten.json()["short_code"]

    await client.get(f"/{code}", follow_redirects=False)

    response = await client.get(f"/{code}/stats")
    assert response.status_code == 200
    data = response.json()
    assert data["click_count"] == 1
    assert data["last_accessed"] is not None


@pytest.mark.asyncio
async def test_stats_country_breakdown(client):
    shorten = await client.post("/shorten", json={"url": "https://stats-country.com"})
    code = shorten.json()["short_code"]

    # testclient IP resolves to None → stored as "unknown"
    await client.get(f"/{code}", follow_redirects=False)
    await client.get(f"/{code}", follow_redirects=False)

    response = await client.get(f"/{code}/stats")
    data = response.json()
    assert data["click_count"] == 2
    assert "unknown" in data["country_breakdown"]
    assert data["country_breakdown"]["unknown"] == 2


@pytest.mark.asyncio
async def test_stats_missing_code(client):
    response = await client.get("/doesnotexist/stats")
    assert response.status_code == 404
    assert response.json()["detail"] == "Short code not found"


@pytest.mark.asyncio
async def test_stats_original_url_preserved(client):
    shorten = await client.post("/shorten", json={"url": "https://preserve-url.com/path?q=1"})
    code = shorten.json()["short_code"]

    response = await client.get(f"/{code}/stats")
    assert response.json()["original_url"] == "https://preserve-url.com/path?q=1"
