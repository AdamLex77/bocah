from importlib import import_module
from platform import python_version

from pytz import timezone
from datetime import datetime

from pyrogram import __version__
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import bot, ubot
from PyroUbot.config import LOGS_MAKER_UBOT
from PyroUbot.core.helpers import PY
from PyroUbot.modules import loadModule

HELP_COMMANDS = {}


async def loadPlugins():
    now = datetime.now(timezone("Asia/Jakarta"))
    time = now.strftime("%d-%m-%Y")
    clock = now.strftime("%H:%M:%S")
    modules = loadModule()
    for mod in modules:
        imported_module = import_module(f"PyroUbot.modules.{mod}")
        module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()
        if module_name:
            HELP_COMMANDS[module_name] = imported_module
    print(f"[🤖 @{bot.me.username} 🤖] [🔥 TELAH BERHASIL DIAKTIFKAN! 🔥]")
    TM = await bot.send_message(
        LOGS_MAKER_UBOT,
        f"""
<b>🤖 ᴜsᴇʀʙᴏᴛ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>
<b>📕 ᴘʏᴛʜᴏɴ: {python_version()}</b>
<b>📙 ᴘʏʀᴏɢʀᴀᴍ: {__version__}</b>
<b>👤 ᴜsᴇʀ: {len(ubot._ubot)}</b>
<b>📆 ᴅᴀᴛᴇ: {time}</b>
<b>⏰ ᴛɪᴍᴇ: {clock}</b>
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("CLOSED", callback_data="0_cls")]],
        ),
    )
    
    

@PY.CALLBACK("0_cls")
async def _(client, callback_query):
    await callback_query.message.delete()
