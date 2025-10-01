CREATE TABLE telethon_sessions (
    id INTEGER PRIMARY KEY,
    telegram_user_id BIGINT,
    phone_number VARCHAR NOT NULL UNIQUE,
    auth_token TEXT NOT NULL,
    phone_code_hash TEXT
);

-- CREATE INDEX idx_sessions_user_id ON telethon_sessions(telegram_user_id);
CREATE INDEX idx_sessions_phone_number ON telethon_sessions(phone_number);
