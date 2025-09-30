# manage.py
import sys
import aiosqlite
from faker import Faker
import random

import db as db_module
import crud


fake = Faker()

async def seed(count: int = 5):
    for _ in range(count):
        telegram_user_id = random.randint(100000000, 999999999)  # фейковый user_id
        auth_token = fake.sha256()  # случайный "токен"
        await crud.add_session(telegram_user_id, auth_token)
    print(f"✅ Inserted {count} fake records")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage.py [create_db|drop_db|reset_db]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "db:create":
        import asyncio
        asyncio.run(db_module.create_db())
    elif command == "db:drop":
        import asyncio
        asyncio.run(db_module.drop_db())
    elif command == "db:reset":
        import asyncio
        asyncio.run(db_module.reset_db())
    elif command == "db:seed":
        import asyncio
        asyncio.run(seed())
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
