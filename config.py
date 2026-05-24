import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# ========== ТВОИ ДАННЫЕ ==========
BOT_TOKEN = "8767025443:AAEJL7q6kyqqRd3RsSW9-45t_2cJvP9bKPGw"
OWNER_ID = 6783350851
CHANNEL_ID = -1002948114104
GROUP_ID = -1002489835677
AUTO_UPDATE_GROUP_ID = True
LOGS_FILE = BASE_DIR / "logs.json"
ALLOWED_FILE = BASE_DIR / "allowed_users.json"
# =================================

def parse_chat_id(value):
    if value is None:
        return None
    if isinstance(value, int):
        return value
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

def set_env_value(key, value):
    os.environ[key] = str(value)

print(f"Загружено: BOT_TOKEN={BOT_TOKEN[:10]}..., OWNER_ID={OWNER_ID}, CHANNEL_ID={CHANNEL_ID}, GROUP_ID={GROUP_ID}")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан!")
if OWNER_ID == 0:
    raise RuntimeError("OWNER_ID не задан или неверен!")
if not CHANNEL_ID:
    raise RuntimeError("CHANNEL_ID не задан!")
if not GROUP_ID:
    raise RuntimeError("GROUP_ID не задан!")
