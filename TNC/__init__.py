from .logging import LOGGER
from TNC.core.dir import dirr
from TNC.core.git import git
from TNC.misc import dbb, heroku

# Initialize basic setup first
dirr()
git()
dbb()
heroku()

# Import Safone API and main bot classes after setup
from SafoneAPI import SafoneAPI
from TNC.core.bot import TNC
from TNC.core.userbot import Userbot

# Initialize clients
app = TNC()
api = SafoneAPI()
userbot = Userbot()

# Import platform APIs (make sure these classes exist in TNC/platforms)
from .platforms import (
    AppleAPI,
    CarbonAPI,
    SoundAPI,
    SpotifyAPI,
    RessoAPI,
    TeleAPI,
    YouTubeAPI,
)

# Initialize platform integrations
Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

LOGGER(__name__).info("TNC package initialized successfully.")