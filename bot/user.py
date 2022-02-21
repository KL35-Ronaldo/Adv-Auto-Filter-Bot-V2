from pyrogram import Client, __version__
from . import API_HASH, API_ID, LOGGER, SESSION_STRING


class User(Client):
    def __init__(self):
        super().__init__(
            session_name=SESSION_STRING,
            api_id=API_ID,
            api_hash=API_HASH,
            workers=4
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Stopped. Bye.")
