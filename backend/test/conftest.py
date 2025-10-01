import pytest
from pathlib import Path
from fastapi.testclient import TestClient
import aiosqlite
from app.app import app
from app.db import get_db


SQL_DIR = Path(__file__).parent.parent / "app"
CREATE_DB = SQL_DIR / "create_db.sql"


async def override_get_db():
    db = await aiosqlite.connect(":memory:")
    db.row_factory = aiosqlite.Row

    with open(CREATE_DB, "r", encoding="utf-8") as f:
        schema = f.read()
    await db.executescript(schema)

    try:
        yield db
    finally:
        await db.close()


def override_get_telegram_user_id():
    return 123456789


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides["get_telegram_user_id"] = override_get_telegram_user_id


@pytest.fixture
def client():
    return TestClient(app)
