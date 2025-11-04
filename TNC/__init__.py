import asyncio
import uvloop

# ✅ Ensure uvloop policy and an active event loop BEFORE importing Pyrogram
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from .logging import LOGGER
from TNC.core.dir import dirr
from TNC.core.git import git
from TNC.misc import dbb, heroku

# ✅ Initialize core setup
dirr()
git()
dbb()
heroku()

# ✅ Import Safone API and main bot classes after event loop setup
from SafoneAPI import SafoneAPI
from TNC.core.bot import TNC
from TNC.core.userbot import Userbot

# ✅ Initialize clients safely
try:
    app = TNC()
except Exception as e:
    LOGGER(__name__).error(f"Failed to initialize TNC bot: {e}")
    app = None

try:
    api = SafoneAPI()
except Exception as e:
    LOGGER(__name__).error(f"Failed to initialize SafoneAPI: {e}")
    api = None

try:
    userbot = Userbot()
except Exception as e:
    LOGGER(__name__).error(f"Failed to initialize Userbot: {e}")
    userbot = None

# ✅ Import platform APIs (make sure these classes exist)
from .platforms import (
    AppleAPI,
    CarbonAPI,
    SoundAPI,
    SpotifyAPI,
    RessoAPI,
    TeleAPI,
    YouTubeAPI,
)

# ✅ Initialize platform integrations
Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

LOGGER(__name__).info("TNC package initialized successfully with uvloop policy.")