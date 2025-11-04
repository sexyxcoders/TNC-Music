import asyncio
import uvloop
import sys
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus
from pytgcalls import idle  # ✅ use pytgcalls.idle if you’re running music features

import config
from ..logging import LOGGER


# ✅ Use uvloop for faster asyncio performance
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class TNC(Client):
    def __init__(self, name="TNCxMUSIC"):
        LOGGER(__name__).info("Initializing Music Bot...")

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
        """Start the Pyrogram bot and check admin permissions."""
        await super().start()

        # ✅ Fetch bot info
        self.me = await self.get_me()
        self.id = self.me.id
        self.name = self.me.first_name + (f" {self.me.last_name}" if self.me.last_name else "")
        self.username = self.me.username
        self.mention = self.me.mention

        # ✅ Log startup info
        LOGGER(__name__).info(f"Bot started as {self.name} (@{self.username})")

        # ✅ Send log message to LOGGER_ID (if configured)
        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"🆔 ID : <code>{self.id}</code>\n"
                    f"👤 Name : {self.name}\n"
                    f"🔗 Username : @{self.username}"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid, ValueError):
            LOGGER(__name__).error(
                "❌ Bot failed to access the log group/channel. "
                "Make sure the bot is added as an admin."
            )
            sys.exit(1)
        except Exception as ex:
            LOGGER(__name__).error(
                f"❌ Unable to send start message. Reason: {type(ex).__name__}"
            )
            sys.exit(1)

        # ✅ Verify admin status in LOGGER_ID
        member = await self.get_chat_member(config.LOGGER_ID, self.id)
        if member.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "❌ Please promote your bot as an admin in your log group/channel."
            )
            sys.exit(1)

        LOGGER(__name__).info("✅ Music Bot fully started and ready.")

    async def stop(self):
        """Stop the bot and cleanup resources."""
        await super().stop()
        LOGGER(__name__).info("🛑 Music Bot stopped cleanly.")


# ===========================================================
# Main runner
# ===========================================================
async def main():
    LOGGER(__name__).info("🚀 Launching TNC Music Bot...")

    bot = TNC()

    try:
        await bot.start()
        LOGGER(__name__).info("🎧 Bot is running. Waiting for events...")
        # ✅ Keep bot alive (PyTgCalls-safe)
        await idle()
    except Exception as e:
        LOGGER(__name__).error(f"❌ Fatal Error: {e}")
    finally:
        await bot.stop()
        # ✅ Close all leftover aiohttp sessions safely
        for task in asyncio.all_tasks():
            task.cancel()

        LOGGER(__name__).info("✅ Event loop closed successfully.")


if __name__ == "__main__":
    uvloop.install()
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        LOGGER(__name__).warning("🧩 Bot stopped manually or by Heroku dyno restart.")