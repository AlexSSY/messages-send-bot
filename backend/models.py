from pydantic import BaseModel


class TelethonSession(BaseModel):
    id: int
    telegram_user_id: int
    auth_token: str
