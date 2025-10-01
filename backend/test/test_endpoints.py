import pytest


@pytest.mark.asyncio
async def test_get_me(client):
    response = client.get("/me")
    assert response.status_code == 200
    data = response.json()
    assert data["telegram_user_id"] == 123456789
