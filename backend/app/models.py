from pydantic import BaseModel
from typing import Any, Optional, Dict


class TelethonSession(BaseModel):
    id: int
    telegram_user_id: int
    phone_number: str
    auth_token: str


class SendCodeRequest(BaseModel):
    phone_number: str


class VerifyCodeRequest(BaseModel):
    phone_number: str
    code: str
    phone_code_hash: str


class SignInRequest(BaseModel):
    phone_number: str
    password: str


class AuthResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
