CREATE TABLE telethon_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- или SERIAL для PostgreSQL
    telegram_user_id BIGINT NOT NULL,
    auth_token TEXT NOT NULL
);

-- индекс для быстрого поиска по telegram_user_id
CREATE INDEX idx_sessions_user_id ON telethon_sessions(telegram_user_id);
