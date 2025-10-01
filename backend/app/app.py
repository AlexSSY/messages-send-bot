from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from aiogram import types
import aiosqlite

from .bot import bot, dp
from .depends import get_telegram_user_id, get_db
from .config import Config
from .models import AuthResponse, SendCodeRequest, VerifyCodeRequest, SignInRequest
from .telegram_client import TelegramClientManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    import os
    os.makedirs("sessions", exist_ok=True)
    await bot.set_webhook(Config.WEBHOOK_URL)
    yield
    await bot.delete_webhook()


load_dotenv()
app = FastAPI(lifespan=lifespan)
query_list = []


origins = [
    "*",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post(Config.WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    update = types.Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)


@app.get("/me")
async def get_me(user_id: int = Depends(get_telegram_user_id)):
    return { "telegram_user_id": user_id }


@app.post("/query")
async def query(user_id: int = Depends(get_telegram_user_id)):
    query_list.append(user_id)
    return {"status" : "ok"}


@app.post("/auth/send-code", response_model=AuthResponse)
async def send_verification_code(
        request: SendCodeRequest, 
        db: aiosqlite.Connection = Depends(get_db), 
        telegram_user_id: int = Depends(get_telegram_user_id)
    ):
    """Send verification code to phone number"""
    telegram_manager = TelegramClientManager(db, telegram_user_id)
    try:
        result = await telegram_manager.send_code_request(request.phone_number)
        
        if result['success']:
            return AuthResponse(
                success=True,
                message="Verification code sent successfully",
                data={
                    "phone_code_hash": result['phone_code_hash'],
                    "timeout": result.get('timeout'),
                    "type": result.get('type')
                }
            )
        else:
            return AuthResponse(
                success=False,
                message="Failed to send verification code",
                error=result.get('error')
            )
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/auth/verify-code", response_model=AuthResponse)
async def verify_code(
        request: VerifyCodeRequest,
        db: aiosqlite.Connection = Depends(get_db),
        telegram_user_id: int = Depends(get_telegram_user_id)
    ):
    """Verify the received code"""
    telegram_manager = TelegramClientManager(db, telegram_user_id)
    try:
        result = await telegram_manager.verify_code(
            phone_number=request.phone_number,
            code=request.code,
            phone_code_hash=request.phone_code_hash
        )
        
        if result['success']:
            return AuthResponse(
                success=True,
                message="Successfully authenticated",
                data={
                    "user": result['user'],
                    "session_file": result['session_file']
                }
            )
        elif result.get('requires_2fa'):
            return AuthResponse(
                success=False,
                message="Two-factor authentication required",
                error="2FA_REQUIRED"
            )
        else:
            return AuthResponse(
                success=False,
                message="Verification failed",
                error=result.get('error')
            )
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/auth/sign-in-2fa", response_model=AuthResponse)
async def sign_in_with_2fa(
        request: SignInRequest,
        db: aiosqlite.Connection = Depends(get_db), 
        telegram_user_id: int = Depends(get_telegram_user_id)
    ):
    """Sign in with 2FA password"""

    try:
        result = await telegram_manager.sign_in_with_password(
            phone_number=request.phone_number,
            password=request.password
        )
        
        if result['success']:
            return AuthResponse(
                success=True,
                message="Successfully authenticated with 2FA",
                data={
                    "user": result['user'],
                    "session_file": result['session_file']
                }
            )
        else:
            return AuthResponse(
                success=False,
                message="2FA authentication failed",
                error=result.get('error')
            )
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))