import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def parse_chat_id(value):
    if value is None:
        return None
    value = str(value).strip()
    if not value:
        return None
    if value.startswith("@"):
        return value
    try:
        return int(value)
    except ValueError:
        return value

def parse_int(value, default=0):
    if value is None:
        return default
    try:
        return int(str(value).strip())
    except (ValueError, AttributeError):
        return default

# Читаем переменные окружения (с Railway или из системы)
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = parse_int(os.getenv("OWNER_ID"), default=0)
CHANNEL_ID = parse_chat_id(os.getenv("CHANNEL_ID"))
GROUP_ID = parse_chat_id(os.getenv("GROUP_ID"))
AUTO_UPDATE_GROUP_ID = os.getenv("AUTO_UPDATE_GROUP_ID", "0") in ("1", "true", "True")
LOGS_FILE = BASE_DIR / os.getenv("LOGS_FILE", "logs.json")
ALLOWED_FILE = BASE_DIR / os.getenv("ALLOWED_FILE", "allowed_users.json")

# Безопасный вывод в лог (проверяем, что токен не None)
token_preview = BOT_TOKEN[:10] if BOT_TOKEN else "ОТСУТСТВУЕТ"
print(f"Загружено: BOT_TOKEN={token_preview}..., OWNER_ID={OWNER_ID}, CHANNEL_ID={CHANNEL_ID}, GROUP_ID={GROUP_ID}")

# Проверки
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан в переменных окружения!")
if OWNER_ID == 0:
    raise RuntimeError("OWNER_ID не задан или неверен!")
if not CHANNEL_ID:
    raise RuntimeError("CHANNEL_ID не задан!")
if not GROUP_ID:
    raise RuntimeError("GROUP_ID не задан!")
