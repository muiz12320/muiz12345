from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/d8f2c7ff9c5c8efc68272.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/5f1651ef2a992cef68f1e.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/vcbotsupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/paid_src")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5090817443").split()))


FAILED = "https://telegra.ph/file/c4154bcb0d00e182ff0d9.jpg"
