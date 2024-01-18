from pyrogram import Client, enums, filters
from pyrogram.types import Message

from PyroUbot import *


async def join(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ...")
    try:
        await xxnx.edit(f"ʙᴇʀʜᴀꜱɪʟ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ᴄʜᴀᴛ ɪᴅ `{Man}`")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"ERROR: \n\n{str(ex)}")


async def leave(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ...")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit("ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴅɪʟᴀʀᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ")
    try:
        await xxnx.edit_text(f"{client.me.first_name} ᴛᴇʟᴀʜ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ɢʀᴜᴘ ɪɴɪ, ʙʏᴇ!!")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"ERROR: \n\n{str(ex)}")


async def kickmeall(client: Client, message: Message):
    Man = await message.reply("ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ ɢʀᴏᴜᴘ...")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"ʙᴇʀʜᴀꜱɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ɢʀᴏᴜᴘ, ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {er} ɢʀᴏᴜᴘ"
    )


async def kickmeallch(client: Client, message: Message):
    Man = await message.reply("ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ...")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"ʙᴇʀʜᴀꜱɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ᴄʜᴀɴɴᴇʟ, ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {er} ᴄʜᴀɴɴᴇʟ"
    )
