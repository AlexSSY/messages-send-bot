import os
from telethon import TelegramClient
from telethon.errors import (
    SessionPasswordNeededError, 
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    PhoneNumberInvalidError
)
from typing import Dict, Any
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TelegramAuthManager:
    def __init__(self):
        self.api_id = int(os.getenv('TELEGRAM_API_ID'))
        self.api_hash = os.getenv('TELEGRAM_API_HASH')
        self.active_clients: Dict[str, TelegramClient] = {}
        self.pending_verifications: Dict[str, Dict] = {}

    async def create_client(self, session_name: str) -> TelegramClient:
        """Create a new Telegram client"""
        client = TelegramClient(
            f"sessions/{session_name}",
            self.api_id,
            self.api_hash
        )
        await client.connect()
        return client

    async def send_code_request(self, phone_number: str) -> Dict[str, Any]:
        """Send verification code and return phone_code_hash"""
        try:
            session_name = f"user_{phone_number}"
            client = await self.create_client(session_name)
            
            # Send code request
            sent_code = await client.send_code_request(phone_number)
            
            # Store client and verification data
            self.active_clients[phone_number] = client
            self.pending_verifications[phone_number] = {
                'phone_code_hash': sent_code.phone_code_hash,
                'client': client
            }
            
            logger.info(f"Verification code sent to {phone_number}")
            
            return {
                'success': True,
                'phone_code_hash': sent_code.phone_code_hash,
                'timeout': sent_code.timeout,
                'type': type(sent_code).__name__
            }
            
        except PhoneNumberInvalidError:
            logger.error(f"Invalid phone number: {phone_number}")
            return {
                'success': False,
                'error': 'Invalid phone number'
            }
        except Exception as e:
            logger.error(f"Error sending code: {str(e)}")
            return {
                'success': False,
                'error': f'Failed to send code: {str(e)}'
            }

    async def verify_code(self, phone_number: str, code: str, phone_code_hash: str) -> Dict[str, Any]:
        """Verify the received code"""
        try:
            if phone_number not in self.pending_verifications:
                return {
                    'success': False,
                    'error': 'No pending verification for this phone number'
                }

            verification_data = self.pending_verifications[phone_number]
            client = verification_data['client']
            
            # Verify the code
            await client.sign_in(
                phone=phone_number,
                code=code,
                phone_code_hash=phone_code_hash
            )
            
            # Get user info
            me = await client.get_me()
            user_info = {
                'id': me.id,
                'first_name': me.first_name,
                'last_name': me.last_name,
                'username': me.username,
                'phone': me.phone
            }
            
            # Clean up pending verification
            del self.pending_verifications[phone_number]
            
            logger.info(f"Successfully verified code for user: {user_info['first_name']}")
            
            return {
                'success': True,
                'user': user_info,
                'session_file': client.session.filename
            }
            
        except SessionPasswordNeededError:
            logger.info("2FA password required")
            return {
                'success': False,
                'requires_2fa': True,
                'message': 'Two-factor authentication required'
            }
        except PhoneCodeInvalidError:
            logger.error("Invalid verification code")
            return {
                'success': False,
                'error': 'Invalid verification code'
            }
        except PhoneCodeExpiredError:
            logger.error("Verification code expired")
            return {
                'success': False,
                'error': 'Verification code has expired'
            }
        except Exception as e:
            logger.error(f"Error verifying code: {str(e)}")
            return {
                'success': False,
                'error': f'Verification failed: {str(e)}'
            }

    async def sign_in_with_password(self, phone_number: str, password: str) -> Dict[str, Any]:
        """Sign in with 2FA password"""
        try:
            if phone_number not in self.pending_verifications:
                return {
                    'success': False,
                    'error': 'No pending verification for this phone number'
                }

            client = self.pending_verifications[phone_number]['client']
            
            # Sign in with password
            await client.sign_in(password=password)
            
            # Get user info
            me = await client.get_me()
            user_info = {
                'id': me.id,
                'first_name': me.first_name,
                'last_name': me.last_name,
                'username': me.username,
                'phone': me.phone
            }
            
            # Clean up pending verification
            del self.pending_verifications[phone_number]
            
            logger.info(f"Successfully signed in with 2FA for user: {user_info['first_name']}")
            
            return {
                'success': True,
                'user': user_info,
                'session_file': client.session.filename
            }
            
        except Exception as e:
            logger.error(f"Error signing in with password: {str(e)}")
            return {
                'success': False,
                'error': f'2FA authentication failed: {str(e)}'
            }

    async def send_message(self, phone_number: str, recipient: str, message: str) -> Dict[str, Any]:
        """Send message using authenticated session"""
        try:
            session_name = f"user_{phone_number}"
            client = await self.create_client(session_name)
            
            if not await client.is_user_authorized():
                return {
                    'success': False,
                    'error': 'User not authenticated'
                }
            
            await client.send_message(recipient, message)
            await client.disconnect()
            
            return {
                'success': True,
                'message': 'Message sent successfully'
            }
            
        except Exception as e:
            logger.error(f"Error sending message: {str(e)}")
            return {
                'success': False,
                'error': f'Failed to send message: {str(e)}'
            }

    async def get_user_info(self, phone_number: str) -> Dict[str, Any]:
        """Get user information from session"""
        try:
            session_name = f"user_{phone_number}"
            client = await self.create_client(session_name)
            
            if not await client.is_user_authorized():
                await client.disconnect()
                return {
                    'success': False,
                    'error': 'User not authenticated'
                }
            
            me = await client.get_me()
            await client.disconnect()
            
            user_info = {
                'id': me.id,
                'first_name': me.first_name,
                'last_name': me.last_name,
                'username': me.username,
                'phone': me.phone
            }
            
            return {
                'success': True,
                'user': user_info
            }
            
        except Exception as e:
            logger.error(f"Error getting user info: {str(e)}")
            return {
                'success': False,
                'error': f'Failed to get user info: {str(e)}'
            }

# Global instance
telegram_manager = TelegramAuthManager()
