import os, time
from os import environ
from translation import Translation


## Main
APP_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN") 
USER_SESSION = os.environ.get("SESSION_FILE")
DATABASE = os.environ.get("DATABASE_URI")
BOT_NAME = os.environ.get("DONLEE_ROBOT", "FLES")
FORCE_CHANNEL = os.environ.get("FORCE_CHANNEL", "Arjun Pradeep")
SAVE_USER = os.environ.get("SAVE_USER", "no").lower()
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "MOVIES CENTRE")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "DONLEE_ROBOT")
DEV_NAME = os.environ.get("DEV_NAME", "Arjun")
DEV_USERNAME = os.environ.get("DEV_USERNAME", "@Arjunbots")
OWNER_ID = set(int(x) for x in os.environ.get("DEV_ID", "1091859969").split())
GROUP = os.environ.get("GROUP", "♂️ Group")
CHANNEL = os.environ.get("CHANNEL", "Updates")
GROUP_LINK = os.environ.get("GROUP_LINK", "t.me/movies_centre_garage_lux")
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", "t.me/Movies_Centre_Main")
FORCE_SUB_TEXT = os.environ.get("FORCE_TEXT", Translation.FSUB_TEXT)
name_button_welcome = "📣 JOIN MY FILM CHANNEL 📣"
welcome_text_custom = "Hey {mention}\nWelcome To {group_name}\n\nThanks For Your Support"
WELCOME_BUTTON_NAME = os.environ.get("WELCOME_BUTTON_NAME", name_button_welcome)
CUSTOM_WELCOME_TEXT = os.environ.get("WELCOME_TEXT", welcome_text_custom)
CUSTOM_WELCOME = os.environ.get("WELCOME_ENABLE_OR_DISABLE", "no").lower()
BOLD = os.environ.get("FILE_CAPTION", "mono")
PHOTO = (environ.get("PHOTOS", "https://telegra.ph/file/537f8ce5f044915b8a4ad.jpg https://telegra.ph/file/537f8ce5f044915b8a4ad.jpg")).split()
SPELLING_MODE = os.environ.get("SPELLING_MODE_TEXT", Translation.SPELLING_TEXT)
#BUTTON_SIZE = bool(os.environ.get("SIZE_BUTTON"))
BUTTON_MODE = os.environ.get("FILE_BUTTONS", "single").lower()
start_uptime = time.time()
