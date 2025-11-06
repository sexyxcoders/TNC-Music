import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# ============================================================
# 🌐 LOAD ENVIRONMENT VARIABLES
# ============================================================
load_dotenv()

# ============================================================
# ⚙️ PYROGRAM API CONFIG
# ============================================================
API_ID = int(getenv("API_ID", "22657083"))
API_HASH = getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")
BOT_TOKEN = getenv("BOT_TOKEN", "")

# ============================================================
# 👑 BOT & OWNER INFO
# ============================================================
OWNER_USERNAME = getenv("OWNER_USERNAME", "TNC_Official")
OWNER_ID = int(getenv("OWNER_ID", "8449801101"))
BOT_USERNAME = getenv("BOT_USERNAME", "TNCXMusicBot")
BOT_NAME = getenv("BOT_NAME", "TNC X MUSIC 🎧")
ASSUSERNAME = getenv("ASSUSERNAME", "TNCXAssistant")

# ============================================================
# 🍃 MONGODB DATABASE
# ============================================================
MONGO_DB_URI = getenv(
    "MONGO_DB_URI",
    "mongodb+srv://TNC_Database_User:TNCXmusic@cluster0.mongodb.net/?retryWrites=true&w=majority&appName=TNCX",
)

# ============================================================
# ⏱️ TIME LIMITS
# ============================================================
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
DURATION_LIMIT = DURATION_LIMIT_MIN * 60

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# ============================================================
# ☁️ HEROKU / GIT SETTINGS
# ============================================================
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "tnc-music")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/sexyxcoders/TNC-Music")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# ============================================================
# 🔗 SUPPORT & COMMUNITY LINKS
# ============================================================
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TNCnetwork")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TNCmeetups")

# URL VALIDATION
for name, link in [("SUPPORT_CHANNEL", SUPPORT_CHANNEL), ("SUPPORT_CHAT", SUPPORT_CHAT)]:
    if link and not re.match(r"^(?:http|https)://", link):
        raise SystemExit(f"[ERROR] {name} URL is invalid. Must start with https://")

# ============================================================
# 🤖 AUTO LEAVE SETTINGS
# ============================================================
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True") == "True"
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

# ============================================================
# 🎵 DOWNLOAD LIMITS
# ============================================================
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# ============================================================
# 🎧 SPOTIFY API
# ============================================================
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# ============================================================
# 🔐 SESSION STRINGS (USERBOTS)
# ============================================================
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")
STRING6 = getenv("STRING_SESSION6", "")
STRING7 = getenv("STRING_SESSION7", "")

# ============================================================
# 🚫 FILTERS & GLOBAL VARS
# ============================================================
BANNED_USERS = filters.user()
adminlist, lyrical, votemode = {}, {}, {}
autoclean, confirmer = [], {}

# ============================================================
# 🖼️ TNC BRAND IMAGES
# ============================================================
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/exw839.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/ddkc5f.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/2nw6zu.jpg"
STATS_IMG_URL = "https://files.catbox.moe/3v8uls.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/1bu0q0.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/1bu0q0.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/1bu0q0.jpg"
SOUNDCLOUD_IMG_URL = "https://files.catbox.moe/1bu0q0.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/1bu0q0.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/dkn1xh.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/dkn1xh.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/dkn1xh.jpg"

# ============================================================
# 💫 TNC REACTIONS & BRAND ELEMENTS
# ============================================================

# 🎧 Reaction emojis used when user starts the bot
TNC_START_REACTS = [
    "🎧", "🔥", "💫", "🎶", "🎵", "💥", "🌈", "✨", "🚀", "❤️"
]

# 🪩 Branded Sticker IDs (TNC animations / vibes)
TNC_STICKERS_ID = [
    "CAACAgUAAxkBAAEB3TdmQe6K2XYQnTNCxBRAND1xkqMmv0AACpQEAAtjJ6VfKBRANDStickerID1",  # 🔥 TNC Logo Vibe
    "CAACAgUAAxkBAAEB3TlmQe7uZjTNCxWaveSticker2Q4AACqQEAAtjJ6VfKTNCBrandingID2",     # 🎧 TNC Wave
    "CAACAgUAAxkBAAEB3TtmQe8xTNCxBeatSticker3zAACrwEAAtjJ6VfKTNCBrandingID3",        # 🎶 TNC Beats
]

# 🩵 TNC BRAND SLOGANS (for captions, messages, embeds)
TNC_BRAND_TAGLINE = "🎧 Powering Music • Powered by TNC Network"
TNC_CREDITS = "© 2025 TNC X Music | A SexyXCoders Project 🚀"

# ============================================================
# ✅ END OF CONFIG
# ============================================================