import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7999460846:AAG9N2_b4kV2_V4MgxJIZLGeFlOClKFH89M")
API_ID = int(os.environ.get("API_ID", "29736812"))
API_HASH = os.environ.get("API_HASH", "d22c2fc9b388eef56e456f546b1d9c1a")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002373501691"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6197171929").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://jackend44:1CamIKdwrLDXuhns@cluster0.nlnbwph.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")

# broadcast settings

BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
MAX_CONCURRENT = int(os.environ.get("MAX_CONCURRENT", "10"))  # Maximum concurrent message sends. You can set this value up to 1000 if you are using a paid broadcast.
UPDATE_INTERVAL = int(os.environ.get("UPDATE_INTERVAL", "2"))  # Update interval in seconds to avoid flood waits
