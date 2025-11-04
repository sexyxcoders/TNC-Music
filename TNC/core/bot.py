import asyncio
import uvloop
import sys

# ✅ Properly set uvloop policy and ensure a loop exists
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus

import config
from ..logging import LOGGER


class TNC(Client):
    def __init__(self, name="TNCxMUSIC"):
        LOGGER(__name__).info("Starting Bot...")

        super().__init__(
            name=name,
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
            parse_mode="html",
        )

    async def start(self):
        await super().start()
        self.me = await self.get_me()
        self.id = self.me.id
        self.name = self.me.first_name + (" " + self.me.last_name if self.me.last_name else "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"ɪᴅ : <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ : {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid, ValueError):
            LOGGER(__name__).error(
                "Bot failed to access the log group/channel. Make sure the bot is added as admin."
            )
            sys.exit(1)
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot failed to access the log group/channel. Reason: {type(ex).__name__}"
            )
            sys.exit(1)

        member = await self.get_chat_member(config.LOGGER_ID, self.id)
        if member.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot as an admin in your log group/channel."
            )
            sys.exit(1)

        LOGGER(__name__).info(f"✅ Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
        LOGGER(__name__).info("🛑 Music Bot stopped cleanly.")


async def main():
    bot = TNC()
    await bot.start()

    # ✅ Keeps the bot alive (especially useful if pytgcalls or tasks run)
    await asyncio.Event().wait()


if __name__ == "__main__":
    # ✅ Safe asyncio run — no race condition, no missing loop
    uvloop.install()
    asyncio.run(main())