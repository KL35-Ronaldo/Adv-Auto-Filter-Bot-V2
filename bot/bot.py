from pyrogram import Client, __version__
from . import SESSION_NAME, API_ID, API_HASH, BOT_TOKEN, WORKERS, PLUGINS, SLEEP_THRESHOLD, LOGGER
from .user import User

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            session_name=SESSION_NAME,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=WORKERS,
            plugins=PLUGINS,
            sleep_threshold=SLEEP_THRESHOLD
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{bot_details.username} Started! "
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Stopped. Bye.")
