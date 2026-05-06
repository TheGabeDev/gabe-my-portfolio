import pytest


@pytest.mark.asyncio
async def test_shorten_valid_url(client):
    response = await client.post("/shorten", json={"url": "https://example.com"})
    assert response.status_code == 201
    data = response.json()
    assert "short_code" in data
    assert len(data["short_code"]) == 7
    assert data["original_url"] == "https://example.com/"
    assert data["short_url"].endswith(data["short_code"])


@pytest.mark.asyncio
async def test_shorten_invalid_url(client):
    response = await client.post("/shorten", json={"url": "not-a-valid-url"})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_shorten_missing_body(client):
    response = await client.post("/shorten", json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_redirect_valid_code(client):
    shorten = await client.post("/shorten", json={"url": "https://example.com"})
    code = shorten.json()["short_code"]

    response = await client.get(f"/{code}", follow_redirects=False)
    assert response.status_code == 301
    assert response.headers["location"] == "https://example.com/"


@pytest.mark.asyncio
async def test_redirect_missing_code(client):
    response = await client.get("/doesnotexist", follow_redirects=False)
    assert response.status_code == 404
    assert response.json()["detail"] == "Short code not found"


@pytest.mark.asyncio
async def test_redirect_increments_click_count(client):
    shorten = await client.post("/shorten", json={"url": "https://click-test.com"})
    code = shorten.json()["short_code"]

    await client.get(f"/{code}", follow_redirects=False)
    await client.get(f"/{code}", follow_redirects=False)

    stats = await client.get(f"/{code}/stats")
    assert stats.json()["click_count"] == 2
